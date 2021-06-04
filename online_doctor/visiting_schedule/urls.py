from django import urls
from django.urls import path
from .views import getVisitingScheduleOnChamberAndSpecialization, createVisitingScheudle

urlpatterns = [
    path(
        'getVisitingScheduleOnChamberAndSpecialization/<str:chamberId>/<str:specializationId>/',
        getVisitingScheduleOnChamberAndSpecialization, 
        name= 'getVisitingScheduleOnChamberAndSpecialization'
        ),
    path('createVisitingScheudle/', createVisitingScheudle, name='createVisitingScheudle')

]
