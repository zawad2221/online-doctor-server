from django.urls import path
from .views import makeAppointment, getAppointmentByPatientId, getBookedPatientNumberOnScheduleIdAndDate,getAppointmentByPatientIdVisitingScheduleIdAndDate, getNewAppointmentOfPatient, getOldAppointmentOfPatient, getAppointmentByDoctorUserIdScheduleIdAndDate, updateAppointment

urlpatterns = [
    path("makeAppointment/", makeAppointment, name="makeAppointment"),
    path("getAppointmentByPatientId/<str:patientId>/", getAppointmentByPatientId, name="getAppointmentByPatientId"),
    path(
        "getBookedPatientNumberOnScheduleIdAndDate/<str:visitingScheduleId>/<str:date>/", 
        getBookedPatientNumberOnScheduleIdAndDate, 
        name="getBookedPatientNumberOnScheduleIdAndDate"
        ),
    path(
        "getAppointmentByPatientIdVisitingScheduleIdAndDate/<str:patientId>/<str:visitingScheduleId>/<str:date>/", 
        getAppointmentByPatientIdVisitingScheduleIdAndDate, 
        name="getAppointmentByPatientIdVisitingScheduleIdAndDate"
        ),
    path(
        "getOldAppointmentOfPatient/<str:patientUserId>/<str:dateOfToday>/", 
        getOldAppointmentOfPatient, 
        name="getOldAppointmentOfPatient"
        ),
    path(
        "getNewAppointmentOfPatient/<str:patientUserId>/<str:dateOfToday>/", 
        getNewAppointmentOfPatient, 
        name="getNewAppointmentOfPatient"
        ),
    path(
        "getAppointmentByDoctorUserIdScheduleIdAndDate/<str:doctorUserId>/<str:visitingScheduleId>/<str:date>/", 
        getAppointmentByDoctorUserIdScheduleIdAndDate, 
        name="getAppointmentByDoctorUserIdScheduleIdAndDate"
        ),
        path(
        "updateAppointment/", 
        updateAppointment, 
        name="updateAppointment"
        )
]