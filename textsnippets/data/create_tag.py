from typing import Union

from django.core.exceptions import ObjectDoesNotExist

from textsnippets.models.tags import Tags
from common.response import Response


class CreateTagsData:

    @staticmethod
    def create(data: str) -> Union[Response, object]:
        try:
            tag = Tags.object.get(title=data)
            return tag
        except ObjectDoesNotExist:
            tag = Tags.object.create(title=data)
            return tag
