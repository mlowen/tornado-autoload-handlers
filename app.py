import asyncio
import tornado.ioloop
import tornado.web

import handlers

if __name__ == '__main__':
    APP = tornado.web.Application(handlers.ROUTES)
    APP.listen(3000)

    tornado.ioloop.IOLoop.current().start()
