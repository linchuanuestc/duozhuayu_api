from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

HOSTNAME = '10.142.97.177'
POST = '2003'
DATABASE = '360cloud_ecs'
USERNAME = '360cloud_ecs'
PASSWORD = '4d72fdbc6633dcb5'

db_url = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    POST,
    DATABASE
)

engine = create_engine(db_url,
        max_overflow = 0,
        pool_size = 50,
        pool_timeout = 3,
        pool_recycle = 3)
Base = declarative_base(engine)

Session = sessionmaker(engine)
session = scoped_session(Session)
