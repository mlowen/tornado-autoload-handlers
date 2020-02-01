from tornado.web import RequestHandler

class HandlerTwo(RequestHandler):
    def get(self):
        self.write('Hello from two')

ROUTE = (r'/two', HandlerTwo)
