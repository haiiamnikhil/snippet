from typing import Type

from django.core.exceptions import ObjectDoesNotExist

from textsnippets.models.tags import Tags
from common.response import Response


class TagsDetailsData:

    @staticmethod
    def get_tag_details_by_id(tag_id: str) -> Type[Response]:
        try:
            tag = Tags.object.get(id=tag_id)
            Response.result = tag
            Response.status = True
            Response.message = ''
        except ObjectDoesNotExist:
            Response.result = []
            Response.status = False
            Response.message = 'Failed to fetch tag'
            Response.error = 'Error'
        return Response
