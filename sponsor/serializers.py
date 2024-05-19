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


class SponsorCreateSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=256)
    phone_number = serializers.CharField(max_length=32)
    sponsor_sum = serializers.IntegerField(default=0)

    class Meta:
        model = models.Sponsor
        fields = (
            "full_name",
            "phone_number",
            "sponsor_sum"
        )

    def create(self, validated_data):
        return models.Sponsor.objects.create(**validated_data)

    def validate_full_name(self, value):
        all_data = models.Sponsor.objects.filter(full_name=value, sponsor_condition="Yangi")
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
        fields = ("full_name", "phone_number", "university", "student_type", "contract")


class StudentUpdateSerializer(serializers.ModelSerializer):
    university = UniversitySerializer()

    class Meta:
        model = models.Student
        fields = ("full_name", "student_type", "university", "contract")
