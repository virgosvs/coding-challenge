import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado import httpclient
import os
import json

ROOT = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(ROOT, 'templates')
STATIC_DIR = os.path.join(ROOT, 'static')
GOOGLE_MAPS_KEY = 'AIzaSyDO245_BwMB3F_blHy84cmIW0aaAIzl9k8'
IPSTACK_KEY = 'abfc98d93414c81cc09e7195a04cbd64'
IPSTACK_URL_PATTERN = "http://api.ipstack.com/%(host)s?access_key=%(access_key)s"


class APIHandler(tornado.websocket.WebSocketHandler):
    @classmethod
    def is_hostname(cls, s):
        """
        Should return True if the value is a string ending
        in a period, followed by a number of letters.
        """
        return None

    def process_message(self, message):
        msg = json.loads(message)
        if msg['msg'] == 'getPosition':
            self.get_position(msg['payload'])
        elif msg['msg'] == 'position':
            self.send_position(msg['payload'])

    def open(self):
        print("Client connected")

    def on_message(self, message):
        self.process_message(message)

    def on_close(self):
        print("WebSocket closed")

    def get_position(self, host_or_ip):
        client = httpclient.HTTPClient()
        api_request_url = IPSTACK_URL_PATTERN % {'host': host_or_ip, 'access_key': IPSTACK_KEY}
        res = client.fetch(api_request_url)
        self.write_message({
            'msg': 'position',
            'payload': res.body.decode('utf-8')
        })

    def send_position(self, payload):
        # write message from python tornado
        self.write_message({
            'msg': 'position',
            'payload': payload
        })


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html", google_maps_key=GOOGLE_MAPS_KEY)

def make_app():
    settings = {
        'debug': True,
        'template_path': TEMPLATE_DIR
    }
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/wsapi/", APIHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, { 'path': STATIC_DIR })
        ], **settings
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
