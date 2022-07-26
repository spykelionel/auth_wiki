from . import views
from django.urls import path

urlpatterns = [
    path("signup/", views.signup, name='signup'),
    path("login/", views.loginpage, name='login'),
    path('logout', views.userlogout, name='logout'),
]
