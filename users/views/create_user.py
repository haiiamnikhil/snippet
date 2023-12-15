from rest_framework import generics
from rest_framework.response import Response

from users.actions.create_user import CreateUserAction


class CreateUser(generics.CreateAPIView):

    @staticmethod
    def post(request, *args, **kwargs):
        data = request.data
        result = CreateUserAction.create(data=data).to_dict()
        return Response(result, status=200)
