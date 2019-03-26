import tornado.web
from db.database_connect import session
import utils.constants

class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        #authcheck
        print('authchecking')

    def finish(self, data=None, errno=utils.constants.ERR_SUC):
        self.log()
        session.close()
        response = {"errno":errno, "errmsg":utils.constants.ERR_DESC[errno], "data":data}
        super(BaseHandler, self).finish(response)

    def log(self):
        print('loging')
