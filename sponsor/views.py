from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from sponsor import models, serializers


class SponsorListAPIView(generics.ListAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("sponsor_condition", "default_sum",)
