from typing import Type

from django.contrib.auth.hashers import make_password

from users.data.create_user import CreateUserData
from common.response import Response


class CreateUserAction:

    @staticmethod
    def create(data: dict) -> Type[Response]:
        password = make_password(data.get('password'))
        data['password'] = password
        user = CreateUserData.create(data=data)
        return user
