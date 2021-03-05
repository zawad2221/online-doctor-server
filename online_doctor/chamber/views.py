from chamber.models import Chamber
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .serializers import ChamberSerializer, LocationSerializer
from custom_user.serializers import CustomUserSerializer
from custom_user.views import userCreate


@csrf_exempt
def chamberRegistration(request):
    if request.method=="POST":
        try:
            data = JSONParser().parse(request)
        except:
            return JsonResponse({'response':'failed to create'}, status = 400)
        print(data['chamberLocation'])
        location = LocationSerializer(data=data['chamberLocation'])
        if location.is_valid():
            location.save()
            data['chamberLocation']=location.data['locationId']
            user = userCreate(data['chamberUser'])
            
            data['chamberUser']=user.userId
            chamber = ChamberSerializer(data=data)
            if chamber.is_valid():
                chamber.save()
                return JsonResponse(chamber.data, status=201)
        return JsonResponse({'response':'failed to create'}, status = 400)
    return HttpResponse("page not found")
    
@csrf_exempt
def getChamberOnSpecializationAndLocation(request, specializationId, min_latitude, max_latitude, min_longitude,max_longitude):
    if request.method=="GET":
        chamber = Chamber.objects.filter(
            visitingschedule__visitingScheduleDoctorId__doctorSpecializationId=specializationId, 
            chamberLocationId__locationLatitude__gte=min_latitude,
            chamberLocationId__locationLatitude__lte=max_latitude,
            chamberLocationId__locationLongitude__gte=min_longitude,
            chamberLocationId__locationLongitude__lte=max_longitude
            )

        chamberSerializer = ChamberSerializer(chamber, many = True)
        #print(chamberSerializer.data)
        return JsonResponse(chamberSerializer.data, status=200, safe=False)