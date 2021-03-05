from django import urls
from django.urls import path
from .views import getChamberOnSpecializationAndLocation, chamberRegistration

urlpatterns = [
    path(
        'getChamberOnSpecializationAndLocation/<str:specializationId>/<str:min_latitude>/<str:max_latitude>/<str:min_longitude>/<str:max_longitude>/', 
        getChamberOnSpecializationAndLocation, 
        name= 'getChamberOnSpecializationAndLocation'
        ),
    path('chamberRegistration/', chamberRegistration, name= 'chamberRegistration'),
]
