from django import urls
from django.urls import path
from .views import getVisitingScheduleOnChamberAndSpecialization, createVisitingSchedule

urlpatterns = [
    path(
        'getVisitingScheduleOnChamberAndSpecialization/<str:chamberId>/<str:specializationId>/',
        getVisitingScheduleOnChamberAndSpecialization, 
        name= 'getVisitingScheduleOnChamberAndSpecialization'
        ),
    path('createVisitingSchedule/', createVisitingSchedule, name='createVisitingSchedule')

]
