import re
from django.contrib import admin
from .models import Fee, DaysOfWeek, VisitingSchedule


class VisitingScheduleModelAdmin(admin.ModelAdmin):
    model = VisitingSchedule
    list_filter = ['visitingScheduleDaysOfWeekId__day','isCanceled']
    search_fields =[
        'visitingScheduleDoctorId__doctorUserId__userName',
        'visitingScheduleChamberId__chamberUserId__userName',
        'startAt',
        'endAt'

    ]
    list_display = [
            "id", 
            "startAt", 
            "endAt", 
            "maxPatient", 
            "isCanceled", 
            "isDeleted", 
            "days_Of_Week", 
            "doctor", 
            "chamber"
    ]
    def id(self, obj):
        return obj.visitingScheduleId
    def days_Of_Week(self, obj):
        return obj.visitingScheduleDaysOfWeekId.day
    def doctor(self, obj):
        return obj.visitingScheduleDoctorId.doctorUserId.userName
    def chamber(self, obj):
        return obj.visitingScheduleChamberId.chamberUserId.userName

admin.site.register(Fee)
admin.site.register(DaysOfWeek)
admin.site.register(VisitingSchedule, VisitingScheduleModelAdmin)

