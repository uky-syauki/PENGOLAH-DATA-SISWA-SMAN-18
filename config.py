import os
import time

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	WTF_CSRF_TIME_LIMIT = None
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-gues'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	os.environ["TZ"] = "Asia/Makassar"
	time.tzset()
