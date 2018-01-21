import os

SECRET_KEY = "This-is-a-secret-key"
DEBUG = True

DB_USERNAME = 'chriszhang94'
DB_PASSWORD = ''
BLOG_DATABASENAME = 'blog'
DB_HOST = os.getenv('IP','0,0,0,0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME,DB_PASSWORD,DB_HOST,BLOG_DATABASENAME)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

POST_PER_PAGE = 5
COMMENT_PER_PAGE = 5
UPLOADED_IMAGES_DEST = '/home/ubuntu/workspace/flask_blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'

MSEARCH_INDEX_NAME = 'whoosh_index'



MSEARCH_BACKEND = 'whoosh'



MSEARCH_ENABLE = True
MAIL_SERVER = 'smtp.buaa.edu.cn'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = '12061008'
MAIL_PASSWORD = '42n-RUL-Pbz-26u'
FLASKY_MAIL_SENDER = 'Flasky Admin <12061008@buaa.edu.cn>'
FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'