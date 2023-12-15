from typing import Type

from textsnippets.data.tag_details import TagsDetailsData
from textsnippets.serializers.snippets import SerializeTags

from common.response import Response


class TagsDetailsAction:

    @staticmethod
    def get_tag_details_by_id(tag_id: str) -> Type[Response]:
        tag = TagsDetailsData.get_tag_details_by_id(tag_id=tag_id)
        if tag.result:
            tag.result = SerializeTags(tag.result, many=False)
        return tag
