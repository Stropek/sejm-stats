from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import serializers

from sejm_app.models.committee import (
    Committee,
    CommitteeMember,
    CommitteeSitting,
    CommitteeType,
)


class CommitteePagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 100


class CommitteeSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    compositionDate = serializers.SerializerMethodField()

    class Meta:
        model = Committee
        fields = [
            "name",
            "nameGenitive",
            "code",
            "compositionDate",
            "phone",
            "scope",
            "type",
        ]

    def get_type(self, obj):
        return CommitteeType(obj.type).label

    def get_compositionDate(self, obj):
        return obj.friendlyCompositionDate


class CommitteeMemberSerializer(serializers.ModelSerializer):
    envoy = serializers.StringRelatedField()

    class Meta:
        model = CommitteeMember
        fields = [
            "committee",
            "envoy",
            "function",
        ]


class CommitteeSittingSerializer(serializers.ModelSerializer):
    committee = serializers.StringRelatedField()
    prints = serializers.StringRelatedField(many=True)

    class Meta:
        model = CommitteeSitting
        fields = [
            "agenda",
            "closed",
            "date",
            "num",
            "remote",
            "video_url",
            "committee",
            "prints",
            "type",
        ]


class CommitteeViewSet(ReadOnlyModelViewSet):
    pagination_class = CommitteePagination
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer


class CommitteeMemberViewSet(ReadOnlyModelViewSet):
    pagination_class = None
    serializer_class = CommitteeMemberSerializer

    def get_queryset(self):
        code = self.request.query_params.get("code")
        if code:
            return CommitteeMember.objects.filter(code=code)
        return CommitteeMember.objects.all()


class CommitteeSittingViewSet(ReadOnlyModelViewSet):
    pagination_class = None
    serializer_class = CommitteeSittingSerializer

    def get_queryset(self):
        code = self.request.query_params.get("code")
        if code:
            return CommitteeSitting.objects.filter(code=code)
        return CommitteeSitting.objects.all()
