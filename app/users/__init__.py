from flask import Blueprint, request, jsonify

from .schemas import UserSchema
from app.services import users_service

users_bp = Blueprint('users', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@users_bp.route('/', methods=['GET'])
def get_users():
    users = users_service.all()
    users = users_schema.dump(users)

    return jsonify(users), 200


@users_bp.route('/', methods=['POST'])
def post_user():
    json_data = request.get_json(force=True)

    UserSchema.validate_password(json_data['password'])

    data = user_schema.load(json_data)

    user = users_service.create(**data)

    result = user_schema.dump(user)

    return jsonify(result), 201


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users_service.get_or_404(user_id)
    user = user_schema.dump(user)

    return jsonify(user), 200


@users_bp.route('/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    json_data = request.get_json(force=True)

    user = users_service.get_or_404(user_id)

    data = user_schema.load(json_data)

    users_service.update(user, **data)

    result = user_schema.dump(user)

    return jsonify(result), 200
