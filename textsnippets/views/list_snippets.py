from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from textsnippets.actions.list_snippets import ListSnippetsAction


class ListSnippets(generics.ListAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        result = ListSnippetsAction.list_all_snippets().to_dict()
        return Response(result, status=200)

