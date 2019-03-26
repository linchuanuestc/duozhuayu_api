from datetime import datetime
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BIGINT, TINYINT, INTEGER 
from db.database_connect import Base, session


class Order(Base):
    __tablename__ = 'dzy_order'
    order_id = Column(BIGINT, primary_key=True, autoincrement=True) #订单id
    uid = Column(BIGINT(unsigned=True), nullable=False, default=0)  #用户id
    books_order_id = Column(BIGINT(unsigned=True), nullable=False, default=0) #订单书批次id
    amount = Column(BIGINT(unsigned=True), nullable=False, default=0) #订单金额
    num = Column(BIGINT(unsigned=True), nullable=False, default=0) #买了多少书
    status = Column(TINYINT(unsigned=True), nullable=False, default=1)  #订单状态
    ctime = Column(INTEGER(unsigned=True), nullable=False, default=0)  #创建时间 unixtimestamp
    mtime = Column(INTEGER(unsigned=True), nullable=False, default=0)  #修改时间 unixtimestamp

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
        person = User(username='lethe',password='212121')
        session.add(person)
        session.commit()
