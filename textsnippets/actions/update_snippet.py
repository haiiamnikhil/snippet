from typing import Type

from textsnippets.data.update_snippet import UpdateSnippetData
from textsnippets.serializers.snippets import SerializeSnippets
from common.response import Response


class UpdateSnippetAction:

    @staticmethod
    def update(data: dict) -> Type[Response]:
        snippet = UpdateSnippetData.update(data=data)
        if snippet.status:
            snippet.result = [SerializeSnippets(snippet.result, many=False).data]
        return snippet
