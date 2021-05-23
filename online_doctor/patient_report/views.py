from .serializers import TestReportSerializer
from django.http.response import HttpResponse, JsonResponse, FileResponse,Http404
import os
from django.conf import settings
from django.shortcuts import render
from .models import TestReport


def getReportByPatientUserId(request, patientUserId):
    if request.method=="GET":
        report = TestReport.objects.filter(prescriptionId__appointmentId__appointmentPatientId__patientUserId=patientUserId).order_by('-testReportId')
        print(len(report))
        reportSerilizer = TestReportSerializer(report, many=True)
        return JsonResponse(reportSerilizer.data, safe=False, status=200)
    return HttpResponse("page not found")

def getDoneReportByPatientUserId(request, patientUserId):
    if request.method=="GET":
        report = TestReport.objects.filter(prescriptionId__appointmentId__appointmentPatientId__patientUserId=patientUserId, isDone=True).order_by('-testReportId')
        print(len(report))
        reportSerilizer = TestReportSerializer(report, many=True)
        return JsonResponse(reportSerilizer.data, safe=False, status=200)
    return HttpResponse("page not found")

def getNotReportByPatientUserId(request, patientUserId):
    if request.method=="GET":
        report = TestReport.objects.filter(prescriptionId__appointmentId__appointmentPatientId__patientUserId=patientUserId, isDone=False).order_by('-testReportId')
        print(len(report))
        reportSerilizer = TestReportSerializer(report, many=True)
        return JsonResponse(reportSerilizer.data, safe=False, status=200)
    return HttpResponse("page not found")

def downloadReportFile(request, reportId):
    report = TestReport.objects.get(testReportId=reportId)
    path = report.filePath.path
    if report.isDone==True:
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/pdf")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                print(response)
                return response
    return HttpResponse("no file found")