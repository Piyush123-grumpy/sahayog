from django.urls import path

from . import views

app_name='fundraise'

urlpatterns = [
    path("", views.donateform, name="donateform")
]