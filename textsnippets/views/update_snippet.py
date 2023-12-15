from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from textsnippets.actions.update_snippet import UpdateSnippetAction


class UpdateSnippet(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def put(self, request, *args, **kwargs):
        data = request.data
        result = UpdateSnippetAction.update(data=data).to_dict()
        return Response(result, status=200)
