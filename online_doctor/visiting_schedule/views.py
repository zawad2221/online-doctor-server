from django.shortcuts import render
from django.http import JsonResponse

from .models import VisitingSchedule, Fee, DaysOfWeek
from .serializers import VisitingScheduleSerializer



def getVisitingScheduleOnChamberAndSpecialization(request, chamberId, specializationId):
    if request.method=="GET":
        visitingSchedule = VisitingSchedule.objects.filter(
            visitingScheduleChamberId__chamberId = chamberId,
            visitingScheduleDoctorId__doctorSpecializationId__specializationId = specializationId
        )
        print(visitingSchedule)
        visitingScheduleSerializer = VisitingScheduleSerializer(visitingSchedule, many = True)
        return JsonResponse(visitingScheduleSerializer.data, status=200, safe=False)
