from typing import Type

from textsnippets.data.create_snippet import CreateSnippetData
from common.response import Response


class CreateSnippetAction:

    @staticmethod
    def create(data: dict) -> Type[Response]:
        snippet = CreateSnippetData.create(data=data)
        return snippet
