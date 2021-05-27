
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from .models import Specialization, Doctor
from .serializers import DoctorSerializer, SpecializationSerializer
from custom_user.serializers import CustomUserSerializer
from custom_user.views import userCreate
from visiting_schedule.models import VisitingSchedule
from visiting_schedule.serializers import VisitingScheduleSerializer
from appointment.models import Appointment

@csrf_exempt 
def getSpecialization(request):
    if request.method=="GET":
        specialization = SpecializationSerializer(Specialization.objects.all(),many=True)
        return JsonResponse(specialization.data, status=200, safe=False)
    return JsonResponse({'response':'failed to get data'}, status=400)

@csrf_exempt
def doctorRegistration(request):
    if request.method=="POST":
        try:
            data = JSONParser().parse(request)
        except:
            return JsonResponse({'response':'bad request'}, status = 400)
        data['doctorSpecialization'] = data['doctorSpecialization']['specializationId']
        user = userCreate(data['doctorUser'])
        
        data['doctorUser']=user.userId
        doctor= DoctorSerializer(data=data)
        if doctor.is_valid():
            doctor.save()
            return JsonResponse(doctor.data, status=201)
        return JsonResponse({'response':'failed to create'}, status = 400)
    return HttpResponse("page not found")

#date to calculate number of patient booked for next schedule
def getVisitingScheduleByDoctorUserId(request, doctorUserId):
    if request.method=="GET":
        visitingSchedule = VisitingSchedule.objects.filter(visitingScheduleDoctorId__doctorUserId=doctorUserId)
        visitingScheduleSerializer = VisitingScheduleSerializer(visitingSchedule, many=True)
        #appointment = Appointment.objects.filter(appointmentVisitingScheduleId__visitingScheduleDoctorId__doctorUserId=doctorUserId, appointmentDate=date)
        #visitingScheduleSerializer.data['numberOfPatientBooked']=len(appointment)
        return JsonResponse(visitingScheduleSerializer.data, status=200, safe=False)
    return HttpResponse("page not found")
    