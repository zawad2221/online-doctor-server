from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Medicine, Prescription
from .serializers import MedicineSerializer, PrescriptionSerializer
from appointment.models import Appointment
from appointment.serializers import AppointmentSerializer

def getPrescriptionByPatientUserId(request,patientUserId):
    if request.method == "GET":
        prescription = Prescription.objects.filter(appointmentId__appointmentPatientId__patientUserId=patientUserId)
        prescriptionSerializer = PrescriptionSerializer(prescription, many=True)
        return JsonResponse(prescriptionSerializer.data, status=200, safe=False)
    return HttpResponse("page not found")

@csrf_exempt
def makePrescription(request):
    if request.method=="POST":
        try:
            data = JSONParser().parse(request)
            print(data['appointment']['appointmentId'])
            appointment = Appointment.objects.get(appointmentId=data['appointment']['appointmentId'])
            appointmentSerializer = AppointmentSerializer(appointment)
            data['appointment'] = appointmentSerializer.data
            data['appointment']["appointmentVisitingSchedule"] = data['appointment']["appointmentVisitingSchedule"]["visitingScheduleId"]
            data['appointment']["appointmentPatient"] = data['appointment']["appointmentPatient"]["patientId"]
            #print(data)
            for prescribedMedicine in data['prescribedMedicine']:
                medicine = Medicine.objects.get(medicineId=prescribedMedicine['medicine']['medicineId'])
                medicineSerializer = MedicineSerializer(medicine)
                prescribedMedicine['medicine']=medicineSerializer.data
            print("data+++++++", data)
            prescriptionSerializer = PrescriptionSerializer(data=data)
            print(prescriptionSerializer.is_valid(raise_exception=True))
            if prescriptionSerializer.is_valid():
                
                print(prescriptionSerializer.validated_data)
                prescriptionSerializer.save()
                #print(prescriptionSerializer.data['prescriptionId'])
                return JsonResponse(prescriptionSerializer.data, status=201)
        except:
            
            return JsonResponse({'response':'bad request'}, status = 400)
            
    return HttpResponse("page not found")