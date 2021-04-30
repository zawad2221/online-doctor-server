from django.urls import path
from .views import patientRegistration, getAskedQueryByPatient,saveAskedQuery

urlpatterns = [
    path('patientRegistration/', patientRegistration, name='patientRegistration'),
    path('getAskedQueryByPatient/<str:patientUserId>/', getAskedQueryByPatient, name='getAskedQueryByPatient'),
    path('saveAskedQuery/', saveAskedQuery, name='saveAskedQuery'),
]
