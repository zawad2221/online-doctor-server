from django.urls import path
from .views import pathologyRegistration
urlpatterns = [
    path('pathologyRegistration/', pathologyRegistration, name='pathologyRegistration')
]
