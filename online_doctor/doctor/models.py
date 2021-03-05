from django.db import models
from django.db.models.fields import AutoField, CharField
from django.db.models.fields.related import ForeignKey
from custom_user.models import User

class Specialization(models.Model):
    specializationId = AutoField(primary_key= True)
    specializationName = CharField(max_length=22)
    specializationDetail = CharField(max_length = 99)

class Doctor(models.Model):
    doctorId= AutoField(primary_key=True)
    doctorBmdcId= CharField(max_length=22)
    doctorDesignation = CharField(max_length=55)
    doctorSpecializationId = ForeignKey(Specialization, on_delete=models.CASCADE)
    doctorUserId = ForeignKey(User, on_delete=models.CASCADE)
