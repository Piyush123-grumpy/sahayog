from django.urls import path

from . import views

app_name='fundraise'

urlpatterns = [
    path("", views.fundraisePage, name="charity"),
    path("category/<int:category>/", views.viewCategory, name="category"),
    path("detail/<int:charity>/", views.viewFundraise, name="viewFundraise"),
]