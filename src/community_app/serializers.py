from django.template.defaultfilters import truncatechars
from rest_framework import serializers

from community_app.models import Article
from sejm_app.utils import format_human_friendly_date


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "content", "image", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
