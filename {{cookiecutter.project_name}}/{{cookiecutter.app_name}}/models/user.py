# coding: utf-8

import datetime

from {{cookiecutter.app_name}}.extensions import db, bcrypt
from flask_login import AnonymousUserMixin


class User(db.Model):
    """ 用户模型 """
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    is_admin = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    def __init__(self, **kwargs):
        """ 创建实例 """
        super(User, self).__init__(**kwargs)
        if self.password:
            self.set_password(self.password)
        else:
            self.password = None

    def __repr__(self):
        """ 将实例表示为唯一字符串 """
        # return "<User %s>" % self.username
        # return '<User {})>'.format(self.username)
        return '<User ({username!r})>'.format(username=self.username)

    def set_password(self, password):
        """ 设置密码 """
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        """ 加密密码 """
        return bcrypt.check_password_hash(self.password, password)

    def is_authenticated(self):
        """ 是否已登录认证 """
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        """ 是否激活 """
        return True

    def is_anonymous(self):
        """ 是否游客 """
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return unicode(self.id)