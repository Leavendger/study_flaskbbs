from flask import Flask
import config
from exts import db, mail, cache, csrf
from flask_migrate import Migrate
from models import auth
from apps.front import front_bp
from bbs_celery import make_celery

# 将ORM模型映射到数据库中三部曲
# 0. migrate = Migrate(app, db)
# 1. flask db init
# 2. flask db migrate
# 3. flask db upgrade

# Python中操作redis安装两个包
# 1. pip install redis
# 2. pip install hiredis

# 在windows上使用celery.需要借助gevent
# pip install gevent
# celery -A app.mycelery --loglevel=info -P gevent

# pip install flask-wtf

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)
cache.init_app(app)
csrf.init_app(app)

migrate = Migrate(app, db)

mycelery = make_celery(app)

# 注册蓝图
app.register_blueprint(front_bp)

if __name__ == '__main__':
    app.run()
