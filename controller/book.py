from modules.book_module import Book 
from controller.base import BaseHandler
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import exc
import utils.util
import utils.constants
import time

#通过bookid批量查询用户信息
class GetBooksHandler(BaseHandler):
    def post(self):
        try:
            ids_str = self.get_body_argument("ids")
            #TO DO 参数检查
            ids = ids_str.split("|")
            books = Book.by_ids(ids)
            book_infos = [] 
            for book in books:
                book_infos.append(utils.util.row_convert_dict(user))
            self.finish({"books": book_infos})
        except NoResultFound:    
            self.finish({}, utils.constants.ERR_NO_BOOK)
        except exc.SQLAlchemyError as e:
            self.finish({}, utils.constants.ERR_DB)
        except: 
            self.finish({}, utils.constants.ERR_UNKNOWN)
