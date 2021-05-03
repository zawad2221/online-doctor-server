from django.urls import path
from .views import patientRegistration, getAskedQueryByPatient,saveAskedQuery, getNotAnsweredQueryByPatient, getAnsweredQueryByPatient

urlpatterns = [
    path('patientRegistration/', patientRegistration, name='patientRegistration'),
    path('getAskedQueryByPatient/<str:patientUserId>/', getAskedQueryByPatient, name='getAskedQueryByPatient'),
    path('getNotAnsweredQueryByPatient/<str:patientUserId>/', getNotAnsweredQueryByPatient, name='getNotAnsweredQueryByPatient'),
    path('getAnsweredQueryByPatient/<str:patientUserId>/', getAnsweredQueryByPatient, name='getAnsweredQueryByPatient'),
    path('saveAskedQuery/', saveAskedQuery, name='saveAskedQuery'),
]
