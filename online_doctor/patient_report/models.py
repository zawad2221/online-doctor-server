from django.db import models
from django.db.models.fields import AutoField, CharField, DateField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from patient.models import Patient
from pathology.models import Pathology
from django.db.models.functions import Coalesce
from datetime import datetime






class PatientReport(models.Model):
    
    def user_directory_path(instance, filename):
        
        filename=str(datetime.date(datetime.now()))+"_"+filename
        # file will be uploaded to MEDIA_ROOT/patient_<id>/patientReport_<id>/<filename>
        return 'file/patient_report/patient_id_{0}/pathology_id_{1}/{2}'.format(instance.patientId.patientId,instance.pathologyId.pathologyId , filename)
    patientReportId = AutoField(primary_key=True)
    sendDate = models.DateTimeField(auto_now_add=True)
    patientId = ForeignKey(Patient, on_delete=models.CASCADE)
    pathologyId = ForeignKey(Pathology, on_delete=models.CASCADE)
    filePath = models.FileField(upload_to=user_directory_path)
    
