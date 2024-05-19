from rest_framework import generics, viewsets, response, renderers, filters
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from sponsor import models, serializers
from http import HTTPMethod
from django.shortcuts import get_object_or_404


class SponsorLisAPIView(generics.ListAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorListSerializer


class SponsorCreateAPIView(generics.CreateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorCreateSerializer


class SponsorRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorListSerializer


# class StudentCreateAPIView(generics.Create)


class StudentAPIView(viewsets.ModelViewSet):

    def get(self, request):
        serializer = serializers.StudentUpdateSerializer
        return response.Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        student = get_object_or_404(models.Student.objects.all(), pk=pk)
        serializer = serializers.StudentCreateSerializer(instance=student, context={"request": request})
        return response.Response(serializer.data)

    def update(self, request, pk=None):
        instance = get_object_or_404(models.Student.objects.all(), pk=pk)
        serializer = serializers.SponsorUpdateSerializer(instance=instance, data=request.data, context={
                                                         "request": request}, partial=True)
        serializer.is_valid()
        serializer.save()
        return response.Response({"data": serializer.data})

    def perform_create(self, serializer):
        full_name = serializer.validated_data.get("full_name")
        phone_number = serializer.validated_data.get("phone_number")
        university = serializer.validated_data.get("university")
        student_type = serializer.validated_data.get("student_type")
        self.get_queryset().create(
            full_name=full_name,
            phone_number=phone_number,
            university=university,
            student_type=student_type
        )

    def get_queryset(self):
        if self.action == "add":
            return []
        else:
            return models.Student.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.StudentCreateSerializer
        return serializers.StudentUpdateSerializer
