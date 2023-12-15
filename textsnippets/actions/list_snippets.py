from typing import Type

from textsnippets.data.list_snippets import ListSnippetsData
from textsnippets.serializers.snippets import SerializeSnippets

from common.response import Response


class ListSnippetsAction:

    @staticmethod
    def list_all_snippets() -> Type[Response]:
        snippets = ListSnippetsData.list_all_snippets()
        serialized = SerializeSnippets(snippets, many=True).data
        Response.result = [{'data': serialized, 'count': len(serialized)}]
        return Response
