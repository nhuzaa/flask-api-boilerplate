from .models import User
from app.common.services import Service


class UsersService(Service):
    __model__ = User

    def _preprocess_params(self, kwargs):
        kwargs.pop('password', None)
        return kwargs
