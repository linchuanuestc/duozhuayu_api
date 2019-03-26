from datetime import datetime
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BIGINT, TINYINT, INTEGER 
from sqlalchemy.orm.exc import NoResultFound
from db.database_connect import Base, session

class User(Base):
    __tablename__ = 'dzy_user'
    uid = Column(BIGINT, primary_key=True, autoincrement=True) #用户id
    username = Column(String(50), nullable=False, default='') #用户名
    head_img = Column(String(200), nullable=False, default='') #头像
    account = Column(BIGINT(unsigned=True), nullable=False, default=0) #账户余额
    buy_num = Column(BIGINT(unsigned=True), nullable=False, default=0) #卖了多少书
    buy_order_num = Column(BIGINT(unsigned=True), nullable=False, default=0) #卖了多少次书
    sell_num = Column(BIGINT(unsigned=True), nullable=False, default=0) #买了多少书
    sell_order_num = Column(BIGINT(unsigned=True), nullable=False, default=0)  #买了多少次书
    src = Column(TINYINT(unsigned=True), nullable=False, default=1)  #用户来源，1=微信
    ctime = Column(INTEGER(unsigned=True), nullable=False, default=0)  #创建时间 unixtimestamp
    mtime = Column(INTEGER(unsigned=True), nullable=False, default=0)  #修改时间 unixtimestamp

    @classmethod
    def by_id(cls, id):
        return session.query(cls).filter_by(uid=id).one()

    @classmethod
    def by_ids(cls, ids):
        return session.query(cls).filter(cls.uid.in_(ids)).all()

    def add_user(self, user):
        session.add(user)
        session.commit()
        return True
