# coding: utf-8

from flask import Blueprint
from flask_restful import Api

from {{cookiecutter.app_name}}.api.resources import UserResource, UserList
from {{cookiecutter.app_name}}.extensions import csrf_protect

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)
csrf_protect.exempt(blueprint)

api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')