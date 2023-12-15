from typing import Type

from django.db import transaction

from textsnippets.models.snippet import Snippet
from textsnippets.data.create_tag import CreateTagsData
from common.response import Response


class CreateSnippetData:

    @staticmethod
    @transaction.atomic
    def create(data: dict) -> Type[Response]:
        try:
            data['tag'] = CreateTagsData.create(data=data.get('tag'))
            snippet = Snippet.object.create(**data)
            Response.result = []
            Response.message = "Snippet Created"
            Response.status = True
        except Exception as e:
            Response.message = "Failed to created Snippet"
            Response.status = False
            Response.error = 'Failed'
            transaction.set_rollback(True)
        return Response
