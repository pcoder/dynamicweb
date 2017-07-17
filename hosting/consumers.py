from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.security.websockets import allowed_hosts_only
from hosting.models import DynamicWebCeleryTaskModel, DynamicWebActionEnumerator
from celery.result import AsyncResult
from hosting.tasks import delete_vm_task
import json
import logging

log = logging.getLogger(__name__)


# @allowed_hosts_only
@channel_session_user_from_http
def ws_connect_hosting(message, vm_id):
    # Accept the incoming connection
    message.reply_channel.send({"accept": True})
    channel_name = message.user.id
    channel_id = 'users_{}_{}'.format(channel_name, vm_id)
    print('Subscribing to {}'.format(channel_id))
    Group(channel_id).add(message.reply_channel)


# @allowed_hosts_only
@channel_session_user
def ws_receive_hosting(message, vm_id):
    channel_name = message.user.id
    channel_id = 'users_{}_{}'.format(channel_name, vm_id)
    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", message)
        return

    if data:
        if data['action'] == "get_vm_state":
            print("in action get_vm_state")
            # check if we have pending tasks (such as terminate_vm) for this vm
            try:
                celery_task = DynamicWebCeleryTaskModel.objects.filter(vm_id=vm_id).last()
                print("after celery_task")
            except DynamicWebCeleryTaskModel.DoesNotExist:
                Group(channel_id).send({
                    "text": json.dumps({
                        "state": "none",
                    })
                })
                return
            print("out")
            if celery_task is None:
                print("celery_task is None")
                json_msg = json.dumps({
                    "state": "none",
                })
                print("sending message")
                Group(channel_id).send({
                    "text": json_msg
                })
                print("sending to channelid {} - msg = {}".format(channel_id, json_msg))
            else:
                print("celery_task is NOT None")
                celery_task_result = AsyncResult(id=celery_task.celery_task_id)
                print("{}".format(celery_task_result.task_id))
                print("{}".format(DynamicWebActionEnumerator(celery_task.action).name))
                print("{}".format(celery_task_result.state))
                print("result is {} {} {}".format(celery_task_result.task_id,
                                                  DynamicWebActionEnumerator(celery_task.action).name,
                                                  celery_task_result.state))
                json_msg = json.dumps({
                    "action": DynamicWebActionEnumerator(celery_task.action).name,
                    "state": celery_task_result.state,
                })
                print("json_msg is {}".format(json_msg))
                Group(channel_id).send({
                    "text": json_msg
                })
                print("sending to channelid {} - msg = {}".format(channel_id, json_msg))

            return

        elif data['action'] == "terminate_vm":
            # Create delete vm celery task
            base_url = "{0}://{1}".format(message.get("scheme", "http"), message.get("host", ""))
            new_celery_task = delete_vm_task.delay(message.user.email, message.user.password, int(vm_id), base_url,
                                                   channel_id)
            job = DynamicWebCeleryTaskModel(
                vm_id=vm_id,
                celery_task_id=new_celery_task.task_id,
                user_id=message.user.id,
                action=DynamicWebActionEnumerator.TERMINATE_VM.value
            )
            job.save()
            # Tell the client that the task has been started
            Group(channel_id).send({
                "text": json.dumps({
                    "action": DynamicWebActionEnumerator(job.action).name,
                    "state": new_celery_task.state,
                    "value": new_celery_task.get(),
                })
            })


@channel_session_user
def ws_disconnect_hosting(message, vm_id):
    channel_name = message.user.id
    Group('users_{}_{}'.format(channel_name, vm_id)).discard(message.reply_channel)
