from django.urls import path
from .views import makeAppointment, getAppointmentByPatientId, getBookedPatientNumberOnScheduleIdAndDate,getAppointmentByPatientIdVisitingScheduleIdAndDate

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
        )
]