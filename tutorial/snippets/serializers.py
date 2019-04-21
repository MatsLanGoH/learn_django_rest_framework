from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `Snippet` Model
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        model = Snippet
        fields = (
            "url",
            "id",
            "highlight",
            "owner",
            "title",
            "code",
            "line_numbers",
            "language",
            "style",
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `User` model
    """

    snippets = serializers.HyperlinkedIdentityField(
        many=True, view_name="snippet-detail", read_only=True
    )

    class Meta:
        model = User
        # FIXME: /users/<int:pk> returns 400
        fields = ("url", "id", "username", "snippets")
