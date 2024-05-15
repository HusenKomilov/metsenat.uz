from rest_framework import serializers
from sponsor import models, choices


class SponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = (
            "id",
            "full_name",
            "phone_number",
            "sponsor_sum",
            "separated",
            "created_ad",
            "sponsor_condition"
        )


class SponsorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = (
            "full_name",
            "phone_number",
            "sponsor_condition",
            "sponsor_sum",
            "transfers",
            "sponsor_type",
            "organization"
        )


class SponsorCreateSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=256)
    phone_number = serializers.CharField(max_length=32)
    default_sum = serializers.ChoiceField(choices=choices.SponsorSum.choices)
    sponsor_sum = serializers.IntegerField(default=0)

    class Meta:
        model = models.Sponsor
        fields = (
            "full_name",
            "phone_number",
            "default_sum",
            "sponsor_sum"
        )

    def create(self, validated_data):
        return models.Sponsor.objects.create(**validated_data)

    def validate_name(self, value):
        all_data = models.Sponsor.objects.filter(full_name=value, sponsor_condition="New")

        if all_data:
            raise serializers.ValidationError("Sizningso'rovingiz ko'rib chiqish uchun yuborilgan")
        else:
            return value


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.University
        fields = ("title",)


class StudentListSerializer(serializers.ModelSerializer):
    university = UniversitySerializer()
    separated = serializers.IntegerField(default=0)

    class Meta:
        model = models.Student
        fields = ("id", "full_name", "student_type", "university", "separated", "contract")


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ("full_name", "student_type", "university", "contract")
