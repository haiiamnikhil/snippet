from typing import Type

from django.db import transaction

from textsnippets.models.snippet import Snippet
from textsnippets.data.create_tag import CreateTagsData
from common.response import Response


class UpdateSnippetData:

    @staticmethod
    @transaction.atomic
    def update(data: dict) -> Type[Response]:
        try:
            snippet_id = data.get('id')
            data['tag'] = CreateTagsData.create(data=data.get('tag'))
            snippet, created = Snippet.object.update_or_create(id=snippet_id, defaults=data)
            Response.result = snippet
            Response.status = True
            Response.message = 'Snippet Updated'
        except:
            Response.result = []
            Response.status = False
            Response.message = 'Snippet Updation failed'
            Response.error = 'Error'
            transaction.set_rollback(True)
        return Response
