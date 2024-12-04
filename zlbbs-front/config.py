import os

SECRET_KEY = 'qweasdzxc'

# 项目的根路径
BASE_DIR = os.path.dirname(__file__)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'pythonbbs'
USERNAME = 'root'
PASSWORD = '1234'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4'.format(username=USERNAME,
                                                                                           password=PASSWORD,
                                                                                           host=HOSTNAME, port=PORT,
                                                                                           db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

# MAIL_USE_TLS：端口号587
# MAIL_USE_SSL：端口号465
# QQ邮箱不支持非加密方式发送邮件
# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
# MAIL_USE_SSL = True
MAIL_USERNAME = "LXXXXXXXXXX@mail.com" 
MAIL_PASSWORD = "dXXXXXXXXXXXXXXX"
MAIL_DEFAULT_SENDER = "LLXXXXXXXXXXr@mail.com"
//请至互联网寻找对应的邮箱发送能力解决方案。
//参考方案：https://blog.csdn.net/hao_13/article/details/132818286


# Celery的redis配置
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

# Flask-Caching的配置
CACHE_TYPE = 'RedisCache'
CACHE_DEFAULT_TIMEOUT = 300
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = 6379
