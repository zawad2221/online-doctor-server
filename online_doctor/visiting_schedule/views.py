from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import VisitingSchedule, Fee, DaysOfWeek
from .serializers import VisitingScheduleSerializer, FeeSerializer
from chamber.models import Chamber
from doctor.models import Doctor


@csrf_exempt
def createVisitingScheudle(request):
    if request.method=="POST":
        try:
            data = JSONParser().parse(request)
            data['visitingScheduleChamber'] = Chamber.objects.get(chamberUserId__userPhoneNumber=data['visitingScheduleChamber']['chamberUser']['userPhoneNumber']).chamberId
            data['visitingScheduleDoctor'] = Doctor.objects.get(doctorUserId=data['visitingScheduleDoctor']['doctorUser']['userId']).doctorId
            data['visitingScheduleDaysOfWeek'] = DaysOfWeek.objects.get(day=data['visitingScheduleDaysOfWeek']['day']).datsOfWeekId
            feeSerializer = FeeSerializer(data=data['visitingScheduleFee'])
            if feeSerializer.is_valid():
                feeSerializer.save()
                data['visitingScheduleFee']= feeSerializer.data['feeId']
                schedule = VisitingScheduleSerializer(data=data)
                if schedule.is_valid():
                    schedule.save()
                    return JsonResponse(schedule.data, status=201)

        except:
            return JsonResponse({'response':'bad request'}, status = 400)
    return HttpResponse("page not found")


def getVisitingScheduleOnChamberAndSpecialization(request, chamberId, specializationId):
    if request.method=="GET":
        try:
            if specializationId=="0":
                visitingSchedule = VisitingSchedule.objects.filter(
                    visitingScheduleChamberId__chamberId = chamberId,
                    isDeleted=False
                )
            else:
                visitingSchedule = VisitingSchedule.objects.filter(
                    visitingScheduleChamberId__chamberId = chamberId,
                    visitingScheduleDoctorId__doctorSpecializationId__specializationId = specializationId,
                    isDeleted=False
                )
            print(visitingSchedule)
            visitingScheduleSerializer = VisitingScheduleSerializer(visitingSchedule, many = True)
            return JsonResponse(visitingScheduleSerializer.data, status=200, safe=False)
        except:
            return HttpResponse("page not found")
        
