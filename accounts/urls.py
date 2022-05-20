from django.urls.conf import include
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='accounts'

urlpatterns = [
    path("login", views.loginPage, name="loginPage"),
    path("register", views.registerPage, name="registerPage"),
    path("success", views.success, name="success"),
]