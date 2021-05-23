from typing import Text
from django.db import models
from django.db.models.fields import AutoField, BooleanField, CharField, DateField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from patient.models import Patient
from pathology.models import Pathology
from django.db.models.functions import Coalesce
from datetime import datetime
from prescription.models import Prescription




class TestType(models.Model):
    typeId = AutoField(primary_key=True)
    typeName = CharField(max_length=111)

class Test(models.Model):
    testId = AutoField(primary_key=True)
    testRate = IntegerField()
    typeId = ForeignKey(TestType, on_delete=models.CASCADE)
    pathologyId = ForeignKey(Pathology, on_delete=models.CASCADE)


class TestReport(models.Model):
    
    def user_directory_path(instance, filename):
        
        #filename=str(datetime.date(datetime.now()))+"_"+filename
        # file will be uploaded to MEDIA_ROOT/patient_<id>/patientReport_<id>/<filename>
        return 'file/patient_report/patient_id_{0}/pathology_id_{1}/{2}/{3}'.format(instance.prescriptionId.appointmentId.appointmentPatientId.patientId,instance.testId.pathologyId.pathologyId ,str(datetime.now()), filename)
    testReportId = AutoField(primary_key=True)
    testReportDetails = TextField()
    issueDate = models.DateField(blank=True, null=True)
    isDone = BooleanField(default=False)
    filePath = models.FileField(upload_to=user_directory_path,blank=True, null=True)
    prescriptionId = ForeignKey(Prescription, on_delete=models.CASCADE)
    testId = ForeignKey(Test, on_delete=models.CASCADE,blank=True,null=True)
    typeId = ForeignKey(TestType, on_delete=models.CASCADE)
    
    
