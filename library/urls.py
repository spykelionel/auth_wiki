from . import views
from django.urls import path

urlpatterns = [
    path('', views.libraries, name='libraries'),
    path('library_detail/<slug:slug>/', views.library_detail, name='library_detail'),
]
