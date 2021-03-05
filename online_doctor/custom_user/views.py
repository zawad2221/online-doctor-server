from django.contrib.auth import authenticate
from django.http.response import HttpResponse, JsonResponse
from custom_user.serializers import CustomUserSerializer
from custom_user.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def login(request):
    if request.method=="POST":
        try:
            data = JSONParser().parse(request)
            print(data)
            user = authenticate(userPhoneNumber=data['userPhoneNumber'], password=data['password'])
            #print(user.check_password(data['userPassword']))
            #print("uesr: ->",user.userName)
        except:
            return JsonResponse({'response':'bad request'}, status = 400)
        userSerializer = CustomUserSerializer(user, many=False)
        if userSerializer.data['userPhoneNumber']==data['userPhoneNumber']:    
            return JsonResponse(userSerializer.data, safe=False, status=200)
        return JsonResponse({"response":"user not found"}, safe=False, status=401)
    return HttpResponse("page not found")

def userCreate(data):
    user = User.objects.create_user(userPhoneNumber=data['userPhoneNumber'], password=data['password'])
    user.userName = data['userName']
    user.userRole = data['userRole']
    user.save()
    return user
    