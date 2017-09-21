# *-*coding=utf-8 *-*
import os

DATABASE = 'mysql'
DIRVE = 'pymysql'
USER = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DB = 'flask'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DATABASE, DIRVE, USER, PASSWORD, HOST, PORT, DB)
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.urandom(24)