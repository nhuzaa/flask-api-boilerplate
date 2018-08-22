from flask import request
from flask_restful import Resource
from marshmallow import exceptions as marsh_exceptions

from .schemas import UserSchema
from app.services import users_service

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UsersResource(Resource):
    def get(self):
        users = users_service.all()
        users = users_schema.dump(users)

        return {'status': 'success', 'data': users}, 200

    def post(self):
        json_data = request.get_json(force=True)

        if not UserSchema.validate_password(json_data['password']):
            return {"status": "error", "data": "Invalid password"}, 422

        try:
            data = user_schema.load(json_data)
        except marsh_exceptions.ValidationError as err:
            return {"status": "error", "data": err.messages}, 422

        user = users_service.create(**data)

        result = user_schema.dump(user)

        return {'status': "success", 'data': result}, 201


class UserResource(Resource):
    def get(self, user_id):
        user = users_service.get_or_404(user_id)
        user = user_schema.dump(user)

        return {'status': 'success', 'data': user}, 200

    def put(self, user_id):
        json_data = request.get_json(force=True)

        user = users_service.get_or_404(user_id)
        if not user:
            return {'message': 'User does not exist'}, 400

        try:
            data = user_schema.load(json_data)
        except marsh_exceptions.ValidationError as err:
            return {"status": "error", "data": err.messages}, 422

        users_service.update(user, **data)

        result = user_schema.dump(user)

        return {"status": 'success', 'data': result}, 200
