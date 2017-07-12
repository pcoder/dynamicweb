from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
import json


@channel_session_user_from_http
def ws_connect(message):
    channelid = 'users_{}'.format(message.user.id)
    print('Subscribing to {}'.format(channelid))
    Group(channelid).add(message.reply_channel)
    Group(channelid).send({
        'text': json.dumps({
            'username': message.user.id,
            'is_logged_in': True
        })
    })


@channel_session_user
def ws_disconnect(message):
    Group('users_{}'.format(message.user.id)).discard(message.reply_channel)
