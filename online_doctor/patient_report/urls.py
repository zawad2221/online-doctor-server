from django.urls import path
from .views import getReportByPatientUserId, getDoneReportByPatientUserId, getNotReportByPatientUserId,downloadReportFile
urlpatterns = [
    path('getReportByPatientUserId/<str:patientUserId>/',getReportByPatientUserId,name='getReportByPatientUserId'),
    path('getDoneReportByPatientUserId/<str:patientUserId>/',getDoneReportByPatientUserId,name='getDoneReportByPatientUserId'),
    path('getNotReportByPatientUserId/<str:patientUserId>/',getNotReportByPatientUserId,name='getNotReportByPatientUserId'),
    path('downloadReportFile/<str:reportId>/',downloadReportFile,name='downloadReportFile')
]
