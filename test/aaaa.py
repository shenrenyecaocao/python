import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# config
DATABASE = 'mysql'
DIRVE = 'pymysql'
USER = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DB = 'flask'

# 'mysql+pymysql://root:123456@localhost:3306/flask'
engine = create_engine('{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DATABASE, DIRVE, USER, PASSWORD, HOST, PORT, DB), echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(125))
    fullname = Column(String(125))
    password = Column(String(125))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True)
    artical = Column(String(125))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
# Session = sessionmaker()
# Session.configure(bind=engine)
session = Session()

# insert
# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
# session.add(ed_user)
# session.commit()

# select
our_user = session.query(User).filter_by(name='ed').first()
print our_user