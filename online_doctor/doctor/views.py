
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
from chamber.models import Chamber
from chamber.serializers import ChamberSerializer
import datetime
from datetime import datetime as dt
import pytz
from django.db.models import Q
from django.shortcuts import get_object_or_404




def searchChamber(request, query):
    if request.method=="GET":
        chamber = Chamber.objects.filter(Q(chamberUserId__userPhoneNumber__contains=query)|Q(chamberUserId__userName__contains=query))
        chamberSerializer = ChamberSerializer(chamber, many=True)
        return JsonResponse(chamberSerializer.data, status=200, safe=False)
    return HttpResponse("page not found")

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
DAYS = {
        "saturday":5,
        "sunday":6,
        "monday":0,
        "tuesday":1,
        "wednesday":2,
        "thursday":3,
        "friday":4

}
def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    print("day ahed",days_ahead)
    if days_ahead < 0: # Target day already happened this week <=
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def getVisitingScheduleByDoctorUserId(request, doctorUserId):
    if request.method=="GET":
        # tz_NY = pytz.timezone('Asia/Dhaka')
        # datetime_NY = dt.now(tz_NY)
        # print("NY time:", datetime_NY.date())
        visitingSchedule = VisitingSchedule.objects.filter(visitingScheduleDoctorId__doctorUserId=doctorUserId)
        visitingScheduleSerializer = VisitingScheduleSerializer(visitingSchedule, many=True)
        for vs in visitingScheduleSerializer.data:
            #d = datetime.date.today()
            tz_NY = pytz.timezone('Asia/Dhaka')
            datetime_NY = dt.now(tz_NY)
            next_schedule_date = next_weekday(datetime_NY.date(), DAYS[vs['visitingScheduleDaysOfWeek']['day']])
            #print(d)
            #vs['numberOfPatientBooked'] = next_schedule_date
            appointment = Appointment.objects.filter(appointmentVisitingScheduleId__visitingScheduleDoctorId__doctorUserId=doctorUserId, appointmentDate=next_schedule_date)
            vs['numberOfPatientBooked']=len(appointment)
        return JsonResponse(visitingScheduleSerializer.data, status=200, safe=False)
    return HttpResponse("page not found")
    