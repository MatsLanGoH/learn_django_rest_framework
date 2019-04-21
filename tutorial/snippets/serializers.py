from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializer for `Snippet` Model
    """

    class Meta:
        model = Snippet
        fields = ("id", "title", "code", "line_numbers", "language", "style")


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for `User` model
    """

    class Meta:
        model = User
        fields = ("id", "username", "snippets")
