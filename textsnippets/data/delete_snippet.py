from typing import Type

from django.db import transaction

from textsnippets.models.snippet import Snippet
from common.response import Response


class DeleteSnippetData:

    @staticmethod
    @transaction.atomic
    def delete(data: dict) -> Type[Response]:
        snippet_id = data.get('id')
        try:
            if data.get('multiple_files') or isinstance(snippet_id, list):
                Snippet.object.filter(id__in=snippet_id).delete()
            else:
                Snippet.object.get(id=snippet_id).delete()
            Response.result = []
            Response.status = True
            Response.message = 'Snippet Deleted'
        except Exception as e:
            Response.result = []
            Response.status = False
            Response.message = 'Snippet Deletion Failed'
            Response.error = 'Error'
            transaction.set_rollback(True)
        return Response
