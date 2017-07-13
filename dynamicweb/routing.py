from channels.routing import route
from hosting.consumers import ws_connect_hosting, ws_disconnect


channel_routing = [
    route('websocket.connect', ws_connect_hosting, path='^/hosting/(?P<channel_name>[a-zA-Z0-9_]+)/$'),
    route('websocket.disconnect', ws_disconnect),
]
