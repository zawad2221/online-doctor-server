from chamber.models import Chamber
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from chamber.serializers import LocationSerializer
from .serializers import PathologySerializer
from custom_user.serializers import CustomUserSerializer
from custom_user.views import userCreate

@csrf_exempt
def pathologyRegistration(request):
    if request.method=="POST":
        try:
            data = JSONParser().parse(request)
        except:
            return JsonResponse({'response':'bad request'}, status = 400)
        location = LocationSerializer(data=data['pathologyLocation'])
        if location.is_valid():
            location.save()
            data['pathologyLocation']=location.data['locationId']
            user = userCreate(data['pathologyUser'])
           
            data['pathologyUser']=user.userId
            chamber = PathologySerializer(data=data)
            if chamber.is_valid():
                chamber.save()
                return JsonResponse(chamber.data, status=201)
        return JsonResponse({'response':'failed to create'}, status = 400)
    return HttpResponse("page not found")