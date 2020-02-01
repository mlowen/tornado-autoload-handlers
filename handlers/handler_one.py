from tornado.web import RequestHandler

class HandlerOne(RequestHandler):
    def get(self):
        self.write('Hello from one')

ROUTE = (r'/one', HandlerOne)
