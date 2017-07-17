from celery import shared_task
from channels import Group
import json
import time
from celery.utils.log import get_task_logger
from opennebula_api.models import OpenNebulaManager
from utils.mailer import BaseEmail
from oca.pool import WrongIdError
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from hosting.models import DynamicWebActionEnumerator

logger = get_task_logger(__name__)


@shared_task
def delete_vm_task(email, password, vm_id, base_url, channel_id):
    """
    Deletes a specified vm by a user
    :param email: The email address used for creating opennebula client
    :param password: The password used for creating opennebula client
    :param vm_id: The id of the VM to be deleted
    :param base_url: The base url to be used in the Email Template
    :param channel_id: The websocket channel to which the response is to be sent
    :return: True if the task is successful, False otherwise
    """

    vm = None
    action = DynamicWebActionEnumerator.TERMINATE_VM.name
    manager = OpenNebulaManager(
        email=email,
        password=password
    )

    try:
        vm = manager.get_vm(vm_id)
    except WrongIdError:
        logger.error('We could not find the requested VM. Please \
                       contact Data Center Light Support.'
                     )
        send_message(channel_id, "FAILURE", action)
        return False
    except ConnectionRefusedError:
        logger.error(
            'We could not load your VM due to a backend connection \
            error. Please try again in a few minutes'
        )
        send_message(channel_id, "FAILURE", action)
        return False

    logger.info("Executing delete VM task: VM.id={}, user.email={}".format(vm.id, email))
    terminated = manager.delete_vm(vm.id)

    if not terminated:
        logger.error(
            'Error terminating VM {}'.format(vm.id)
        )
    else:
        context = {
            'vm': vm,
            'base_url': base_url
        }
        email_data = {
            'subject': _('Virtual machine plan canceled'),
            'from_address': settings.DCL_SUPPORT_FROM_ADDRESS,
            'to': email,
            'context': context,
            'template_name': 'vm_status_changed',
            'template_path': 'hosting/emails/'
        }
        base_email = BaseEmail(**email_data)
        base_email.send()

        vm = manager.get_vm_details_from_server(vm_id)
        while vm.str_state != 'DONE':
            time.sleep(2)
            vm = manager.get_vm_details_from_server(vm_id)
            print("VM state = " + vm.str_state)
        print("VM state = " + vm.str_state)

    # Tell the client that the task has finished successfully
    send_message(channel_id, "SUCCESS", action)
    return terminated


def send_message(channel, result, action):
    Group(channel).send({
        "text": json.dumps({
            "result": result,
            "action": action
        })
    })


@shared_task
def add(x, y):
    return x + y
