from flask import Blueprint
from flask_restful import Api
from .apis import UsersResource, UserResource

users_bp = Blueprint('users', __name__)

users_api = Api(users_bp)
users_api.add_resource(UsersResource, '/users')
users_api.add_resource(UserResource, '/users/<int:user_id>')
