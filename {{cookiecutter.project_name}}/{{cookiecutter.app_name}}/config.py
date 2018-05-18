# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    # difference between os.getenv() and os.environ.get()
    SECRET_KEY = os.environ.get('{{cookiecutter.project_name | upper}}_SECRET', 'secret-key')  # TODO: Change me
    # SECRET_KEY = os.getenv('{{cookiecutter.project_name | upper}}_SECRET', default='secret-key')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'

    # 管理后台设置默认账号和密码
    ADMIN_USER = 'admin'
    ADMIN_PASSWORD = '123456'

    SMSBAO_SETTINGS = dict(
        user=os.environ.get('SMSBAO_USER', 'youruser'),
        password=os.environ.get('SMSBAO_PASSWORD', 'yourpassword')
    )


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO: Change me
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar

    MONGODB_SETTINGS = {
        'db': '{{cookiecutter.project_name | lower}}',
        'host': 'localhost',
        'port': 27017
    }

    # mail
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USERNAME = 'username'
    MAIL_PASSWORD = 'password'

    # celery
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
    CELERY_BACKEND = 'amqp://guest:guest@localhost:5672//'


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    SQLALCHEMY_ECHO = False     # print sql string
    DEBUG_TB_ENABLED = True
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.

    MONGODB_SETTINGS = {
        'db': '{{cookiecutter.project_name | lower}}',
        'host': 'localhost',
        'port': 27017
    }

    # mail
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USERNAME = 'username'
    MAIL_PASSWORD = 'password'
    MAIL_SUBJECT_PREFIX = 'xx科技'

    # celery
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
    CELERY_BACKEND = 'amqp://guest:guest@localhost:5672//'

    # Debug toolbar panels
    DEBUG_TB_PANELS = [
        'flask_mongoengine.panels.MongoDebugPanel',
        'flask_debugtoolbar.panels.versionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
    ]



class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
