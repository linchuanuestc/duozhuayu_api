from datetime import datetime
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BIGINT, TINYINT, INTEGER 
from db.database_connect import Base, session

class Book(Base):
    __tablename__ = 'dzy_book' #书信息表
    bid = Column(BIGINT, primary_key=True, autoincrement=True) #book id
    title = Column(String(200), nullable=False, default='') #书名
    sub_title = Column(String(200), nullable=False, default='') #书副标题
    cover_img = Column(String(200), nullable=False, default='') #封面图
    author = Column(String(100), nullable=False, default='') #作者
    publisher = Column(String(100), nullable=False, default='') #出版社
    isbn = Column(String(30), nullable=False, default='') #ISBN
    description = Column(String(200), nullable=False, default='') #备注
    seller = Column(BIGINT(unsigned=True), nullable=False, default=0) #卖家
    level = Column(TINYINT(unsigned=True), nullable=False, default=1)  #品相
    cost = Column(BIGINT(unsigned=True), nullable=False, default=0) #收购成本价
    ctime = Column(INTEGER(unsigned=True), nullable=False, default=0)  #创建时间 unixtimestamp

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def by_ids(cls, ids):
        return session.query(cls).filter(cls.bid.in_(ids)).all()

    def add_book(self, book):
        session.add(book)
        session.commit()
