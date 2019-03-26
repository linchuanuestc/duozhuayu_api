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
