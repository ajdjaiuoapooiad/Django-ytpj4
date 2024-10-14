from django.urls import path
from useradmin import views


urlpatterns = [
    path("", views.Studio, name="studio"),

]