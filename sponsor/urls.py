from django.urls import path
from sponsor import views

urlpatterns = [
    path("sponsor/", views.SponsorListAPIView.as_view()),
]
