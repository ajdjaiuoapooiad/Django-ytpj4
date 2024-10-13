
from django.urls import path
from userauths import *
from userauths.views import RegisterView

urlpatterns = [
   path("sign-up/", RegisterView, name="sign-up"),
]