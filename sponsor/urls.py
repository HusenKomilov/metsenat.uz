from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from sponsor import views

router = DefaultRouter()

router.register(r"sponsor", views.SponsorUpdateAPIView, basename="sponsor")


urlpatterns = [
    path("sponsors/", views.SponsorListAPIView.as_view()),
    path("", include(router.urls)),
    # path("sponsor/<int:pk>/", views.SponsorUpdateAPIView.as_view({"get": "retrieve"})),
]
