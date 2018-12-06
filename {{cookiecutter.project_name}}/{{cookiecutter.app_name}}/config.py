# -*- coding: utf-8 -*-
"""Application configuration."""
import os
from datetime import timedelta


class Config(object):
    """Base configuration."""

    # difference between os.getenv() and os.environ.get()
    # SECRET_KEY = os.environ.get('{{cookiecutter.project_name | upper}}_SECRET_KEY', 'yourSecretKey')
    SECRET_KEY = os.getenv('{{cookiecutter.project_name | upper}}_SECRET_KEY', 'yourSecretKey')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    FILE_FOLDER = os.path.join(PROJECT_ROOT, 'files')
    DATA_FOLDER = os.path.join(PROJECT_ROOT, 'data')
    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'

    # site name and version
    SITE_NAME = '{{cookiecutter.site_name}}'
    VERSION = '{{cookiecutter.version}}'

    # admin user and password
    ADMIN_USER = 'admin'
    ADMIN_PASSWORD = '123456'

    BABEL_DEFAULT_LOCALE = 'zh_Hans_CN' # zh_CN or zh_Hans_CN
    BABEL_DEFAULT_TIMEZONE = 'Asia/Shanghai'

    MONGODB_SETTINGS = {
        'db': '{{cookiecutter.project_name | lower}}',
        'host': 'localhost',
        'port': 27017
    }

    # 文件存储配置选项
    MEDIA_PATH = ''        # 媒体存储路径, 如： '/home/xx/'
    STORAGE_SETTINGS = dict(
        storage_type='local',       # 存储类型
        # base_extensions=dict(),
        auto_remove=False,           # 默认原记录字段上传新文件是否需要删除旧文件
        base_link='/uploads/%s',    # 虚拟路径
        base_dir='uploads',         # 媒体文件存储目录名
        base_path= MEDIA_PATH or FILE_FOLDER, # 媒体文件存储路径
    )

    # Debug toolbar panels
    DEBUG_TB_PANELS = [
        'flask_mongoengine.panels.MongoDebugPanel',
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
    ]

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


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing


class AdminConfig(Config):
    """ Admin configuration """
    SESSION_COOKIE_NAME = '{{cookiecutter.project_name | lower}}.admin'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    INDEX_REDIRECT = '/admin/'

    DEBUG_TB_ENABLED = False