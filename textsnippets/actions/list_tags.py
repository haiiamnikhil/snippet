from typing import Type

from textsnippets.data.list_tags import ListTagsData
from common.response import Response

from textsnippets.serializers.snippets import SerializeTags


class ListTagsAction:

    @staticmethod
    def list_all_tags() -> Type[Response]:
        tags = ListTagsData.list_all_tags()
        if tags:
            Response.result = SerializeTags(tags, many=True)
        return Response
