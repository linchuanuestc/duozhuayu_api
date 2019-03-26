import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import config
import app

def main():
    application = app.Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(config.options["port"])
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
