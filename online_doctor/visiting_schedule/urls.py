from django import urls
from django.urls import path
from .views import getVisitingScheduleOnChamberAndSpecialization

urlpatterns = [
    path(
        'getVisitingScheduleOnChamberAndSpecialization/<str:chamberId>/<str:specializationId>/',
        getVisitingScheduleOnChamberAndSpecialization, 
        name= 'getVisitingScheduleOnChamberAndSpecialization'
        )
]
