from django.urls import path
from .views import getPrescriptionByPatientUserId, makePrescription

urlpatterns = [
    path('getPrescriptionByPatientUserId/<str:patientUserId>/', getPrescriptionByPatientUserId, name='getPrescriptionByPatientUserId'),
    path('makePrescription/', makePrescription, name='makePrescription')
]
