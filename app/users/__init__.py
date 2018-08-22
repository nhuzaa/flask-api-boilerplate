from flask import Blueprint, request, jsonify
from marshmallow import exceptions as marsh_exceptions

from .schemas import UserSchema
from app.services import users_service

users_bp = Blueprint('users', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@users_bp.route('/', methods=['GET'])
def get_users():
    users = users_service.all()
    users = users_schema.dump(users)

    return jsonify({'status': 'success', 'data': users}), 200


@users_bp.route('/', methods=['POST'])
def post_user():
    json_data = request.get_json(force=True)

    if not UserSchema.validate_password(json_data['password']):
        return jsonify({"status": "error", "data": "Invalid password"}), 422

    try:
        data = user_schema.load(json_data)
    except marsh_exceptions.ValidationError as err:
        return jsonify({"status": "error", "data": err.messages}), 422

    user = users_service.create(**data)

    result = user_schema.dump(user)

    return jsonify({'status': "success", 'data': result}), 201


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users_service.get_or_404(user_id)
    user = user_schema.dump(user)

    return jsonify({'status': 'success', 'data': user}), 200


@users_bp.route('/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    json_data = request.get_json(force=True)

    user = users_service.get_or_404(user_id)
    if not user:
        return jsonify({'message': 'User does not exist'}), 400

    try:
        data = user_schema.load(json_data)
    except marsh_exceptions.ValidationError as err:
        return jsonify({"status": "error", "data": err.messages}), 422

    users_service.update(user, **data)

    result = user_schema.dump(user)

    return jsonify({"status": 'success', 'data': result}), 200
