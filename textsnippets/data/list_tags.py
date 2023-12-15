from textsnippets.models.tags import Tags


class ListTagsData:

    @staticmethod
    def list_all_tags():
        tags = Tags.object.filter()
        return tags
