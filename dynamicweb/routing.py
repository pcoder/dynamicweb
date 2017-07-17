from channels.routing import route
from hosting.consumers import ws_connect_hosting, ws_receive_hosting, ws_disconnect_hosting

channel_routing = [
    route('websocket.connect', ws_connect_hosting, path='^/hosting/(?P<vm_id>[^/]+)/$'),
    route("websocket.receive", ws_receive_hosting, path='^/hosting/(?P<vm_id>[^/]+)/$'),
    route('websocket.disconnect', ws_disconnect_hosting, path='^/hosting/(?P<vm_id>[^/]+)/$'),
]
