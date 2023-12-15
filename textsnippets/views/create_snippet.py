from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from textsnippets.actions.create_snippet import CreateSnippetAction


class CreateSnippet(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        data = request.data
        user = self.request.user
        data['user'] = user
        result = CreateSnippetAction.create(data=data).to_dict()
        return Response(result, status=200)
