from django.conf.urls import url
from django.urls import path
from .views import getSpecialization, doctorRegistration, getVisitingScheduleByDoctorUserId, searchChamber

urlpatterns = [
    path('getSpecialization/',getSpecialization, name='getSpecialization'),
    path('doctorRegistration/',doctorRegistration, name='doctorRegistration'),
    path('getVisitingScheduleByDoctorUserId/<str:doctorUserId>/', getVisitingScheduleByDoctorUserId, name='getVisitingScheduleByDoctorUserId'),
    path('searchChamber/<str:query>/', searchChamber, name='searchChamber')

]
