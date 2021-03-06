# coding: utf-8

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from {{cookiecutter.app_name}}.models import User
from {{cookiecutter.app_name}}.extensions import ma, db
from {{cookiecutter.app_name}}.commons.pagination import paginate


class UserSchema(ma.Schema):

    # password = ma.String(load_only=True, required=True)

    class Meta:
        model = User
        sqla_session = db.session
        # Fields to expose
        fields = ('username', 'email', 'password')


class UserResource(Resource):
    """ Single object resource """
    method_decorators = [jwt_required]

    def get(self, user_id):
        schema = UserSchema()
        user = User.query.get_or_404(user_id)
        return {"user": schema.dump(user).data}

    def put(self, user_id):
        schema = UserSchema(partial=True)
        user = User.query.get_or_404(user_id)
        user, errors = schema.load(request.json, instance=user)
        if errors:
            return errors, 422

        return {"msg": "user updated", "user": schema.dump(user).data}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return {"msg": "user deleted"}


class UserList(Resource):
    """ Creation and get_all """
    method_decorators = [jwt_required]

    def get(self):
        schema = UserSchema(many=True)
        query = User.query
        return paginate(query, schema)

    def post(self):
        schema = UserSchema()
        user, errors = schema.load(request.json)
        if errors:
            return errors, 422

        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        u = User(username=username, email=email, password=password)
        db.session.add(u)
        db.session.commit()

        return {"msg": "user created", "user": schema.dump(user).data}, 201
