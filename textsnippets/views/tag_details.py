from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from textsnippets.actions.tag_details import TagsDetailsAction


class TagDetails(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    @staticmethod
    def get(request, tag_id, *args, **kwargs):
        result = TagsDetailsAction.get_tag_details_by_id(tag_id=tag_id).to_dict()
        return Response(result, status=200)
