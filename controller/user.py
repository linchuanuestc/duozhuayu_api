from modules.user_module import User
from controller.base import BaseHandler
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import exc
import utils.util
import utils.constants
import time

#通过uid查询用户信息
class GetUserHandler(BaseHandler):
    def post(self):
        try:
            uid = self.get_body_argument("uid")
            #TO DO 参数检查
            user = User.by_id(uid)
            self.finish({"user":utils.util.row_convert_dict(user)})
        except NoResultFound:    
            self.finish({}, utils.constants.ERR_NO_USER)
        except exc.SQLAlchemyError as e:
            self.finish({}, utils.constants.ERR_DB)
        except: 
            self.finish({}, utils.constants.ERR_UNKNOWN)

class AddUserHandler(BaseHandler):
    def post(self):
        try:
            name = self.get_body_argument("name", "", True)
            head_img_url = self.get_body_argument("head_img", "", True)
            source = self.get_body_argument("src", 1, True)
            #TO DO 参数检查
            now_time = int(time.time())
            user = User(username = name, head_img = head_img_url, src = source, ctime = now_time, mtime = now_time) 
            user.add_user(user) 
            self.finish({"ret": True})
        except exc.SQLAlchemyError:
            self.finish({"ret": False}, utils.constants.ERR_DB)
        except: 
            self.finish({"ret": False}, utils.constants.ERR_UNKNOWN)
