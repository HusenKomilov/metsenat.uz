from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from sponsor import views

router = DefaultRouter()

# router.register(r"sponsor", views.SponsorAPIView, basename="sponsor")
router.register(r"student", views.StudentAPIView, basename="student")


urlpatterns = [
    path("sponsor/", views.SponsorLisAPIView.as_view()),
    path("sponsor/create/", views.SponsorCreateAPIView.as_view()),
    path("sponsor/<int:pk>/", views.SponsorRetriveUpdateAPIView.as_view()),
    # path("students/", views.StudentListAPIView.as_view()),
    path("", include(router.urls)),
]
