# -*- coding: utf-8 -*-

import sys
import pymysql as db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

# config
DATABASE = 'mysql'
DIRVE = 'pymysql'
USER = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DB = 'flask'

Base = declarative_base()
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
# 'mysql+pymysql://root:123456@localhost:3306/flask'
engine = create_engine('{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DATABASE, DIRVE, USER, PASSWORD, HOST, PORT, DB), echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

user = User():
sys.exit()

ed_user = User(id=1, name='Jones')
session.add(ed_user)
session.commit()
session.close()

# connect = db.connect('127.0.0.1', 'root', '123456', 'itme')

# with connect:
#     cursor = connect.cursor()
#     # cursor.execute('SELECT VERSION()')
#     cursor.execute('SELECT * FROM it_role')

#     print cursor.rowcount
#     data = cursor.fetchall()
#     # for i in range(cursor.rowcount):
#     #     row = cursor.fetchone()
#     #     print row[0], row[1]
#     print data

