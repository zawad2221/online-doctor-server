from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display =(
        'patientId','patient_name','phone_number','gender','dateOfBirth','bloodGroup'
    )
    search_fields = [
        'patientUserId__userName'
    ]
    list_filter = (
        'patientGender','patientBloodGroup',
    )
    
    def gender(self, obj):
        return obj.patientGender

    def dateOfBirth(self, obj):
        return obj.patientDateOfBirth
    
    def bloodGroup(self, obj):
        return obj.patientBloodGroup

    def patient_name(self, obj):
        return obj.patientUserId.userName

    def phone_number(self, obj):
        return obj.patientUserId.userPhoneNumber
    
    patient_name.admin_order_field = 'patientUserId__userName'
    phone_number.admin_order_field = 'patientUserId__userPhoneNumber'
    dateOfBirth.admin_order_field = 'patientDateOfBirth'
    gender.admin_order_field= 'patientGender'
    bloodGroup.admin_order_field='patientBloodGroup'

admin.site.register(Patient,PatientAdmin)