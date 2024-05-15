from rest_framework import generics, viewsets, response, renderers
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from sponsor import models, serializers
from django.shortcuts import get_object_or_404


class SponsorListAPIView(generics.ListAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("sponsor_condition", "default_sum",)


class SponsorUpdateAPIView(viewsets.ModelViewSet):
    lookup_field = "pk"

    def list(self, request):
        queryset = self.get_queryset()
        return response.Response({"MED": queryset})

    def retrieve(self, request, pk=None):
        user = get_object_or_404(models.Sponsor.objects.all(), pk=pk)
        serializer = serializers.SponsorUpdateSerializer(user, context={"request": request})
        return response.Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(models.Sponsor.objects.all(), pk=pk)
        serializer = serializers.SponsorUpdateSerializer(
            instance, data=request.data, context={'request': request}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({"data": serializer.data})

    def create(self, request):
        serializer = serializers.SponsorCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"data": serializer.data})
        return response.Response(serializer.errors)

    def get_serializer_class(self):
        if self.action == "update":
            return serializers.SponsorUpdateSerializer
        else:
            return serializers.SponsorCreateSerializer

    def get_queryset(self):
        if self.action == "list" or "get":
            return []
        elif self.action == "put" or "post":
            return models.Sponsor.objects.all()


class StudentListAPIView(generics.ListAPIView):
    queryset = models.Student.objects.all().select_related("university")
    serializer_class = serializers.StudentListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("student_type", "university")


class CreateStudent(generics.CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentCreateSerializer
