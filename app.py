import tornado.web
import controller.user
import controller.book

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                (r"/user/getUser", controller.user.GetUserHandler),
                (r"/user/addUser", controller.user.AddUserHandler),
                (r"/book/getBooks", controller.book.GetBooksHandler)
                ]
        super(Application,self).__init__(handlers)
