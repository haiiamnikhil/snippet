from rest_framework import serializers

from textsnippets.models.snippet import Snippet
from textsnippets.models.tags import Tags


class SerializeTags(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = '__all__'


class SerializeSnippets(serializers.ModelSerializer):
    tag = SerializeTags(many=False)

    class Meta:
        model = Snippet
        fields = '__all__'
