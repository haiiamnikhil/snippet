from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from textsnippets.actions.delete_snippet import DeleteSnippetAction


class DeleteSnippet(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    @staticmethod
    def delete(request, *args, **kwargs):
        data = request.data
        result = DeleteSnippetAction.delete(data=data).to_dict()
        return Response(result, status=200)
