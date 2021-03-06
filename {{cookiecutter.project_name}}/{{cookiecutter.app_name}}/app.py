# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""

from flask import Flask, render_template

from {{cookiecutter.app_name}} import auth, api, commands
from {{cookiecutter.app_name}}.models import User
from {{cookiecutter.app_name}}.extensions import (
    bcrypt, cache, csrf_protect, db, debug_toolbar, 
    login_manager, migrate, webpack, jwt, 
    ma, mail, rest_api, celery)
from {{cookiecutter.app_name}}.config import ProdConfig


def create_app(config_object=ProdConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """

    # app = Flask(__name__)
    # app = Flask('{{cookiecutter.app_name}}')
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)
    return app


def register_extensions(app):
    """ Register Flask extensions. """

    bcrypt.init_app(app)
    cache.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    # webpack.init_app(app)
    jwt.init_app(app)
    # If db is SQLAlchemy instance,
    # Flask-SQLAlchemy must be initialized before Flask-Marshmallow
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    rest_api.init_app(app)
    celery.init_app(app)


def register_blueprints(app):
    """ Register Flask blueprints. """

    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)


def register_errorhandlers(app):
    """ Register error handlers. """

    def render_error(error):
        """ 渲染HTML模板响应错误 """

        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code

    def response_error(error):
        """ 返回json响应错误"""
        error_code = getattr(error, 'code', 500)
        # https://docs.python.org/3/library/http.html#http.HTTPStatus
        # error需要通过str()来序列化
        # if error_code == 400:
        #     return make_response(jsonify(dict(code=error_code, msg=str(error))), HTTPStatus.BAD_REQUEST)
        # if error_code == 401:
        #     return make_response(jsonify(dict(code=error_code, msg=str(error))), HTTPStatus.UNAUTHORIZED)
        # if error_code == 404:
        #     return make_response(jsonify(dict(code=error_code, msg=str(error))), HTTPStatus.NOT_FOUND)
        # if error_code == 500:
        #     return make_response(jsonify(dict(code=error_code, msg=str(error))), HTTPStatus.INTERNAL_SERVER_ERROR)
        return make_response(jsonify(dict(code=error_code, msg=str(error))), error_code)

    for errcode in [400, 401, 404, 500]:
        # app.errorhandler(errcode)(render_error)
        app.errorhandler(errcode)(response_error)


def register_shellcontext(app):
    """ Register shell context objects. """

    def shell_context():
        """Shell context objects."""
        # 将User import 导包到flask shell里的上下文
        return dict(db=db, User=User)

    app.shell_context_processor(shell_context)


def register_commands(app):
    """ Register Click commands. """

    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
