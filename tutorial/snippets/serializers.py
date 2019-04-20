from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializer for `Snippet` Model
    """

    class Meta:
        model = Snippet
        fields = ("id", "title", "code", "line_numbers", "language", "style")
