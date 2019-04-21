from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializer for `Snippet` Model
    """

    class Meta:
        model = Snippet
        fields = ("id", "title", "code", "line_numbers", "language", "style", "owner")

    owner = serializers.ReadOnlyField(source="owner.username")


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for `User` model
    """

    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        # FIXME: /users/<int:pk> returns 400
        fields = ("id", "username", "snippets")
