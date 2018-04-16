# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""

# from passlib.context import CryptContext
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_webpack import Webpack
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from flask_restful import Api
from flask_celery import Celery

# pwd_context = CryptContext(schemes=['pbkdf2_sha256'], deprecated='auto')bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
login_manager = LoginManager()
db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
migrate = Migrate()
cache = Cache()
debug_toolbar = DebugToolbarExtension()
webpack = Webpack()
mail = Mail()
rest_api = Api()
celery = Celery()
