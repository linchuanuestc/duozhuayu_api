from datetime import datetime
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BIGINT, TINYINT, INTEGER 
from db.database_connect import Base, session


class BookOrderBatch(Base):
    __tablename__ = 'dzy_book_order_batch'
    book_order_batch_id = Column(BIGINT, primary_key=True, autoincrement=True) #购买书批次id
    book_id = Column(BIGINT(unsigned=True), nullable=False, default=0) #book id
    buy_user_id = Column(BIGINT(unsigned=True), nullable=False, default=0) #购书用户id
    ctime = Column(INTEGER(unsigned=True), nullable=False, default=0)  #创建时间 unixtimestamp

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def by_id(cls, id):
        return session.query(cls).filter_by(id=id).all()

    @classmethod
    def by_name(cls, name):
        return session.query(cls).filter_by(username=name).all()

    def __repr__(self):
        return "<User(id='%s', " \
               "username='%s', " \
               "password='%s', " \
               "email='%s', " \
               "phone_number='%s', " \
               "id_card='%s', " \
               "createtime='%s', " \
               "_locked='%s'\n)>" % (
                self.id,
                self.username,
                self.password,
                self.email,
                self.phone_number,
                self.id_card,
                self.createtime,
                self._locked
        )

    def add_user(self):
        # 添加单个对象
        # person = User(username='lethe',password='212121')
        # session.add(person)

        # 添加多个对象
        session.add_all([User(username='banban', password='1212120'),
                         User(username='kuku', password='32321')])
        # 提交才会生效，和命令行有区别
        session.commit()
