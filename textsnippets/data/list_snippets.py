from textsnippets.models.snippet import Snippet


class ListSnippetsData:

    @staticmethod
    def list_all_snippets() -> list:
        snippets = Snippet.object.all()
        return snippets
