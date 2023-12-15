from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from textsnippets.actions.snippet_details import SnipperDetailsAction


class SnippetDetails(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    @staticmethod
    def get(request, snippet_id, *args, **kwargs):
        result = SnipperDetailsAction.get_snippet_details_by_id(snippet_id=snippet_id).to_dict()
        return Response(result, status=200)
