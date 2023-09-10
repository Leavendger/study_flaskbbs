# flask_sqlalchemy

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_caching import Cache
from flask_wtf import CSRFProtect

db = SQLAlchemy()
mail = Mail()
cache = Cache()
csrf = CSRFProtect()
