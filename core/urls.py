from django.urls import path
from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("watch/<int:pk>/", views.videoDetail, name="video-detail"),
]