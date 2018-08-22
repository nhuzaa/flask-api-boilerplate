from werkzeug.security import generate_password_hash

from .models import User
from app.common.services import Service


class UsersService(Service):
    __model__ = User

    def _preprocess_params(self, kwargs):
        password = kwargs.pop('password', None)
        if password:
            password = generate_password_hash(password)
            kwargs['password'] = password
        return kwargs
