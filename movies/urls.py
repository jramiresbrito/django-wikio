from django.urls import path
from . import views

# Urls configuration
urlpatterns = [
    path('', views.index, name='index')
]
