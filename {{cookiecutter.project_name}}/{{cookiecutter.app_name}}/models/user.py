# coding: utf-8

from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from {{cookiecutter.app_name}}.extensions import db, bcrypt


class User(db.Model, UserMixin):
    """ 用户模型 """
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=True)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, default=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    is_admin = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

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
        # return '<User {}>'.format(self.username)
        return '<User {username!r}>'.format(username=self.username)

    def __unicode__(self):
        return self.username

    @property
    def is_active(self):
        """ 是否激活 """
        return True

    @property
    def is_authenticated(self):
        """ 是否已登录认证 """
        # if isinstance(self, AnonymousUserMixin):
        #     return False
        # else:
        #     return True
        return False

    @property
    def is_anonymous(self):
        """ 是否游客 """
        # if isinstance(self, AnonymousUserMixin):
        #     return True
        # else:
        #     return False
        return False

    def get_id(self):
        """ 返回一个能够识别唯一用户的ID """
        # return unicode(self.id)
        return str(self.id)

    def set_password(self, password):
        """ 设置密码 """
        # 在python3中，你需要使用在generate_password_hash()上使用decode('utf-8')方法
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """ 加密密码 """
        return bcrypt.check_password_hash(self.password, password)
