from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.security.websockets import allowed_hosts_only
import json
import logging

log = logging.getLogger(__name__)


@allowed_hosts_only
@channel_session_user_from_http
def ws_connect_hosting(message, channel_name):
    # Accept the incoming connection
    message.reply_channel.send({"accept": True})
    channel_id = 'users_{}'.format(channel_name)
    print('Subscribing to {}'.format(channel_id))
    Group(channel_id).add(message.reply_channel)


@allowed_hosts_only
@channel_session_user_from_http
def ws_receive_hosting(message, channel_name):
    channel_id = 'users_{}'.format(channel_name)
    try:
        data = json.loads(message)
    except ValueError:
        log.debug("ws message isn't json text=%s", message)
        return

    if data:
        if data['action'] == "delete_vm":
            # Tell client task has been started
            Group(channel_id).send({
                "text": json.dumps({
                    "action": "started",
                })
            })


@channel_session_user
def ws_disconnect(message):
    Group('users_{}'.format(message.user.id)).discard(message.reply_channel)
