from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from appointment.serializers import AppointmentSerializer
from .models import Appointment
from patient.models import Patient

def test(request):
            data = JSONParser().parse(request)
            # appointment = getAppointmentByDate(data["appointmentDate"])
            # data["appointmentSerialNumber"] = len(appointment)+1
            
            # appointmentSerializer = AppointmentSerializer(data=data)
            # patient = Patient.objects.get(patientUserId=int(data["appointmentPatient"]["patientUser"]["userId"]))
            # print("appointment by date ",patient.patientId)
            # #print("appointment patinet",.patientId)
            appointmentSerializer = AppointmentSerializer(data=data)
            print("appointment by date ",appointmentSerializer.is_valid())
            

@csrf_exempt
def makeAppointment(request):
    if request.method =="POST":
        #test(request)
        try:
            data = JSONParser().parse(request)
            print(data)
            ##check if slot is availabel



            appointment = getAppointmentByDateSchedule(data["appointmentDate"],data["appointmentVisitingSchedule"]["visitingScheduleId"])
            if len(appointment)>= int(data["appointmentVisitingSchedule"]["maxPatient"]):
                print("full................")
                return JsonResponse({"additionalProperties":{"status":"full"}}, status=200, safe=False)
            if len(getAlreadyBookedAppointment(
                data["appointmentPatient"]["patientUser"]["userId"],
                data["appointmentVisitingSchedule"]["visitingScheduleId"],
                data["appointmentDate"]
            )):
                return JsonResponse({"additionalProperties":{"status":"already booked"}}, status=400, safe=False)
            data["appointmentSerialNumber"] = len(appointment)+1
            data["appointmentTime"] = getAppointmentTime(
                data["appointmentVisitingSchedule"]["startAt"],
                data["appointmentVisitingSchedule"]["endAt"],
                data["appointmentVisitingSchedule"]["maxPatient"],
                data["appointmentSerialNumber"]
                )
            data["appointmentIsConfirmed"]=False
            data["appointmentIsCanceled"]=False
            data["appointmentIsVisited"]=False
            data["appointmentVisitingSchedule"] = data["appointmentVisitingSchedule"]["visitingScheduleId"]
            data["appointmentPatient"] = Patient.objects.get(patientUserId=int(data["appointmentPatient"]["patientUser"]["userId"])).patientId
            del(data["additionalProperties"])
            appointmentSerializer = AppointmentSerializer(data=data)
            print("appointment by date ",appointmentSerializer.is_valid())
            # print("appointment time",getAppointmentTime(
            #     data["appointmentVisitingSchedule"]["startAt"],
            #     data["appointmentVisitingSchedule"]["endAt"],
            #     data["appointmentVisitingSchedule"]["maxPatient"],
            #     data["appointmentSerialNumber"]
            #     )
            # )
            print("appointment data ", data)
            if appointmentSerializer.is_valid():
                appointmentSerializer.save()
                return JsonResponse(appointmentSerializer.data, status=201)
            
        except Exception:
            print(Exception)
            return JsonResponse({"response":"bad request"}, status=400)
    
    return HttpResponse("page not found")

def getAlreadyBookedAppointment(patientId, visitingScheduleId, date):
    return Appointment.objects.filter(
            appointmentPatientId__patientUserId=patientId, 
            appointmentVisitingScheduleId = visitingScheduleId,
            appointmentDate = date
            )
#if the patient has a appointment on a specific visiting schedule in upcomming date
def getAppointmentByPatientIdVisitingScheduleIdAndDate(request, patientId, visitingScheduleId, date):
    if request.method=="GET":
        appointment = getAlreadyBookedAppointment(patientId, visitingScheduleId, date)
        appointmentSerializer = AppointmentSerializer(appointment, many = True)
        return JsonResponse(appointmentSerializer.data, status=200, safe= False)
    else:
        return HttpResponse("page not found")

def getAppointmentByPatientId(request, patientId):
    #test(request)
    if request.method =="GET":
        patient = Patient.objects.get(patientUserId=int(patientId))
        appointment = Appointment.objects.filter(appointmentPatientId=patient.patientId)
        appointmentSerializer = AppointmentSerializer(appointment, many = True)
        return JsonResponse(appointmentSerializer.data, status=200, safe= False)
    else:
        return HttpResponse("page not found")

def getBookedPatientNumberOnScheduleIdAndDate(request, visitingScheduleId, date):
    if request.method=="GET":
        appointment = getAppointmentByDateSchedule(date, visitingScheduleId)
        appointmentSerializer = AppointmentSerializer(appointment, many =True)
        size = len(appointment)
        return JsonResponse({"additionalProperties":{"bookedPatientNumber":size}}, status=200, safe=False)
    else:
        return HttpResponse("bad request")


#return visited appointment
def getOldAppointmentOfPatient(request, patientUserId, dateOfToday):
    if request.method=="GET":
        appointment = Appointment.objects.filter(appointmentPatientId__patientUserId__userId = patientUserId, appointmentDate__lt = dateOfToday)
        appointmentSerializer = AppointmentSerializer(appointment, many =True)
        print(len(appointment))
        return JsonResponse(appointmentSerializer.data, status=200, safe=False)
    else:
        return HttpResponse("bad request")
#return upcomming appointment
def getNewAppointmentOfPatient(request, patientUserId, dateOfToday):
    if request.method=="GET":
        appointment = Appointment.objects.filter(appointmentPatientId__patientUserId__userId = patientUserId, appointmentDate__gte = dateOfToday)
        appointmentSerializer = AppointmentSerializer(appointment, many =True)
        print(len(appointment))
        return JsonResponse(appointmentSerializer.data, status=200, safe=False)
    else:
        return HttpResponse("bad request")


def getAppointmentByDateSchedule(date, scheduleId):
    return Appointment.objects.filter(appointmentDate = date, appointmentVisitingScheduleId=scheduleId)

def getHourFromTime(time):
    return str(time).split(":")[0]

def getMinuteFromTime(time):
    return str(time).split(":")[1]

def convertTimeInMinute(time):
    hour = getHourFromTime(time)
    minute = getMinuteFromTime(time)
    return (60*int(hour))+int(minute)

def getAppointmentDurationInMinute(startAt, endAt):
    startAtInMinute = convertTimeInMinute(startAt)
    endAtInMinute = convertTimeInMinute(endAt)
    return endAtInMinute - startAtInMinute

def getPerPatientVisitingTime(durationInMinute, maxPatient):
    return durationInMinute / int(maxPatient)

def getHourMinuteFromMinute(time):
    time = int(time)
    hour = int(time / 60)
    minute = time % 60
    return str(hour)+":"+str(minute)

def getAppointmentTime(startAt,endAt,maxPatient,serial):
    durationInMinute = getAppointmentDurationInMinute(startAt, endAt)
    perPatientVisitingTimeInMinute = getPerPatientVisitingTime(durationInMinute, maxPatient)
    
    timeToAddStartAt = getHourMinuteFromMinute(
        perPatientVisitingTimeInMinute * (int(serial)-1)
    )
    print("timeToAdd: ", timeToAddStartAt)
    appointmentTimeHour = int(getHourFromTime(startAt)) + int(getHourFromTime(timeToAddStartAt))
    appointmentTimeMinute = int(getMinuteFromTime(startAt)) + int(getMinuteFromTime(timeToAddStartAt))
    return str(appointmentTimeHour)+":"+str(appointmentTimeMinute)+":00"
    

    

