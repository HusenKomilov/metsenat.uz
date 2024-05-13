from rest_framework import serializers
from sponsor import models


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = ("id", "full_name", "phone_number", "sponsor_sum", "separated", "created_ad", "sponsor_condition")
