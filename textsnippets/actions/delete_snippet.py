from typing import Type

from textsnippets.data.delete_snippet import DeleteSnippetData

from common.response import Response


class DeleteSnippetAction:

    @staticmethod
    def delete(data: dict) -> Type[Response]:
        snippet = DeleteSnippetData.delete(data)
        return snippet
