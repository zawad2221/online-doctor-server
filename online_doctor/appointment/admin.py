import re
from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    list_display = [
        'appointmentId',
        'patientSymptomNote',
        'appointmentTime',
        # 'appointmentIsConfirmed',
        # 'appointmentIsCanceled',
        # 'appointmentIsVisited',
        'appointmentDate',
        'visitingSchedule',
        'patient'
    ]
    search_fields = [
        'appointmentPatientId__patientUserId__userPhoneNumber',
        'appointmentPatientId__patientUserId__userName',
        'appointmentDate'
    ]
    list_filter = [
        'appointmentIsConfirmed',
        'appointmentIsCanceled',
        'appointmentIsVisited'
    ]
    
    def patientSymptomNote(self, obj):
        return obj.appointmentPatientSymptomNote
    def visitingSchedule(self, obj):
        return obj.appointmentVisitingScheduleId.visitingScheduleId
    def patient(self, obj):
        return obj.appointmentPatientId.patientUserId.userPhoneNumber

    visitingSchedule.admin_order_field = 'appointmentVisitingScheduleId__visitingScheduleId'
    patient.admin_order_field = 'appointmentPatientId__patientUserId__userPhoneNumber'
    patientSymptomNote.admin_order_field = 'appointmentPatientSymptomNote'

admin.site.register(Appointment, AppointmentAdmin)