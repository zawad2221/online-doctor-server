from django.contrib import admin
from .models import Doctor,Specialization

class SpecializationAdmin(admin.ModelAdmin):
    list_display=(
        'specializationId', 'specializationName'
    )

class DoctorAdmin(admin.ModelAdmin):
    list_display=(
        'doctorId', 'doctorPhoneNumber', 'doctorName', 'specialization'
    )
    search_fields = [
        'doctorUserId__userName', 'doctorUserId__userPhoneNumber','doctorSpecializationId__specializationName'
    ]

    list_filter =[
        'doctorSpecializationId__specializationName'
    ]
    def doctorPhoneNumber(self, obj):
        return obj.doctorUserId.userPhoneNumber
    def doctorName(self, obj):
        return obj.doctorUserId.userName
    def specialization(self, obj):
        return obj.doctorSpecializationId.specializationName

    doctorPhoneNumber.admin_order_field = 'doctorUserId__userPhoneNumber'
    doctorName.admin_order_field = 'doctorUserId__userName'
    specialization.admin_order_field = 'doctorSpecializationId__specializationName'
    

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialization, SpecializationAdmin)
