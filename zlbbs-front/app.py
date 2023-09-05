from flask import Flask
import config
from exts import db
from flask_migrate import Migrate
from models import auth

# 将ORM模型映射到数据库中三部曲
# 0. migrate = Migrate(app, db)
# 1. flask db init
# 2. flask db migrate
# 3. flask db upgrade


app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
