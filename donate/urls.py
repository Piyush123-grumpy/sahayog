from django.urls import path

from . import views

app_name='donate'

urlpatterns = [
    path("fundraiseDetail/<int:id>", views.donateform, name="donateform")
]