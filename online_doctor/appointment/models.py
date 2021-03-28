from django.db import models
from django.db.models.fields import AutoField, BooleanField, CharField, DateField, IntegerField, TimeField, TextField
from django.db.models.fields.related import ForeignKey
from visiting_schedule.models import VisitingSchedule
from patient.models import Patient

class Appointment(models.Model):
    appointmentId = AutoField(primary_key=True)
    appointmentPaymentCredential = CharField(max_length=11, blank= True)
    appointmentPatientSymptomNote = TextField(blank= True)
    appointmentTime = TimeField()
    appointmentIsConfirmed = BooleanField(default=False,blank= True)
    appointmentIsCanceled = BooleanField(default=False,blank= True)
    appointmentIsVisited = BooleanField(default=False,blank= True)
    appointmentDate = DateField()
    appointmentSerialNumber = IntegerField()
    appointmentVisitingScheduleId = ForeignKey(VisitingSchedule, on_delete= models.CASCADE)
    appointmentPatientId = ForeignKey(Patient, on_delete= models.CASCADE)

    def __int__(self):
        return self.appointmentId