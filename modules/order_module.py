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
