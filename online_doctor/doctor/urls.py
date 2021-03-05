from django.conf.urls import url
from django.urls import path
from .views import getSpecialization, doctorRegistration

urlpatterns = [
    path('getSpecialization/',getSpecialization, name='getSpecialization'),
    path('doctorRegistration/',doctorRegistration, name='doctorRegistration')
]
