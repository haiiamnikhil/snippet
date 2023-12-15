from typing import Type

from django.core.exceptions import ObjectDoesNotExist, ValidationError

from textsnippets.models.snippet import Snippet
from common.response import Response


class SnippetDetailsData:

    @staticmethod
    def get_snippet_details_by_id(snippet_id: str) -> Type[Response]:
        try:
            snippet = Snippet.object.get(id=snippet_id)
            Response.status = True
            Response.result = snippet
        except ObjectDoesNotExist:
            Response.status = False
            Response.message = 'No data available for this id'
            Response.error = 'Error'
        except ValidationError:
            Response.status = False
            Response.message = 'Id is not correct'
            Response.error = 'Error'
        return Response
