from typing import Type

from textsnippets.data.snippet_details import SnippetDetailsData
from textsnippets.serializers.snippets import SerializeSnippets

from common.response import Response


class SnipperDetailsAction:

    @staticmethod
    def get_snippet_details_by_id(snippet_id: str) -> Type[Response]:
        snippet = SnippetDetailsData.get_snippet_details_by_id(snippet_id=snippet_id)
        snippet.result = [SerializeSnippets(snippet.result, many=False).data]
        return snippet
