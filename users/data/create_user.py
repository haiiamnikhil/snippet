from typing import Type

from django.core.exceptions import ObjectDoesNotExist

from users.models.users import Users
from common.response import Response


class CreateUserData:

    @staticmethod
    def create(data: dict) -> Type[Response]:
        try:
            user = Users.objects.create_user(**data)
            Response.status = True
            Response.message = 'User Created'
            return Response
        except Exception as e:
            Response.message = f"User with same User Id or Email already exists"
            Response.status = False
            Response.error = 'Unique Value Required'
            return Response
