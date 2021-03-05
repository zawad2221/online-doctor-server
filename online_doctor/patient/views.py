from rest_framework import parsers
from chamber.models import Chamber
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .serializers import PatientSerializer
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