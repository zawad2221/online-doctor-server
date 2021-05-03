from rest_framework import parsers
from django.db.models import Q
from chamber.models import Chamber, AskedQuery
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Patient

from .serializers import PatientSerializer, PatientQuerySerializer
from chamber.serializers import AskedQuerySerializer
from custom_user.serializers import CustomUserSerializer
from custom_user.views import userCreate

@csrf_exempt
def patientRegistration(request):
    if request.method=="POST":
        try:
            data = JSONParser().parse(request)
            print("patinet: ",data)
        except:
            return JsonResponse({'response':'bad request'}, status = 400)
        #user = CustomUserSerializer(data=data['patientUser'])
        user = userCreate(data['patientUser'])
        
        data['patientUser']=user.userId
        patient = PatientSerializer(data=data)
        if patient.is_valid():
            patient.save()
            return JsonResponse(patient.data, status=201)
        return JsonResponse({"response":"failed"},status=400)
    return HttpResponse("page not found")

def getAskedQueryByPatient(request, patientUserId):
    if request.method =="GET":
        askedQuery = AskedQuery.objects.filter(queryId__patientId__patientUserId__userId=patientUserId)
        #print(askedQuery['askedQueryAnswer'])
        askedQuerySerializer = AskedQuerySerializer(askedQuery, many = True)
        return JsonResponse(askedQuerySerializer.data, status=200, safe=False)
    return HttpResponse("page not found")

def getAnsweredQueryByPatient(request, patientUserId):
    if request.method =="GET":
        askedQuery = AskedQuery.objects.filter(
            ~Q(askedQueryAnswer =""),
            queryId__patientId__patientUserId__userId=patientUserId
            )
        askedQuerySerializer = AskedQuerySerializer(askedQuery, many = True)
        return JsonResponse(askedQuerySerializer.data, status=200, safe=False)
    return HttpResponse("page not found")

def getNotAnsweredQueryByPatient(request, patientUserId):
    if request.method =="GET":
        askedQuery = AskedQuery.objects.filter(
            queryId__patientId__patientUserId__userId=patientUserId,
            askedQueryAnswer=""
            )
        askedQuerySerializer = AskedQuerySerializer(askedQuery, many = True)
        return JsonResponse(askedQuerySerializer.data, status=200, safe=False)
    return HttpResponse("page not found")

@csrf_exempt
def saveAskedQuery(request):
    if request.method=="POST":
        print("post")
        try:
            data = JSONParser().parse(request)
            patient = Patient.objects.get(patientUserId__userId=data['query']['patient']['patientUser']['userId'])
            data['query']['patient']=patient.patientId
            patientQuery = PatientQuerySerializer(data=data['query'])
            if patientQuery.is_valid():
                patientQuery.save()
                data['query']=patientQuery.data['queryId']
                data['chamber']=data['chamber']['chamberId']
                askedQuery = AskedQuerySerializer(data=data)
                if askedQuery.is_valid():
                    askedQuery.save()
                    ##print("valid")
                    return JsonResponse(askedQuery.data, status=201)
        except:
            return JsonResponse({'response':'bad request'}, status = 400)
    return HttpResponse("page not found")