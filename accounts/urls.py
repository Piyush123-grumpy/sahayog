from django.urls.conf import include
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='accounts'

urlpatterns = [
    path("login", views.loginPage, name="loginPage"),
<<<<<<< HEAD
    path("register", views.registerPage, name="registerPage"),
    path("success", views.success, name="success"),
=======
    # path("register", views.registerPage, name="registerPage"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
>>>>>>> forgetpassword
]