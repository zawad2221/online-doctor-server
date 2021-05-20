from django.db import models
from django.db.models.fields import AutoField, CharField, DateField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from custom_user.models import User


class Patient(models.Model):
    GENDERS = (
        ('male','male'),
        ('female','female'),
        ('others','others')
    )
    BLOOD_GROUPS = (
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-')
    )
    patientId = AutoField(primary_key=True)
    patientNid = CharField(max_length= 33)
    patientGender = CharField(max_length=11, choices= GENDERS)
    patientBloodGroup = CharField(max_length=11, choices= BLOOD_GROUPS)
    patientDateOfBirth = DateField()
    patientUserId = ForeignKey(User, on_delete=models.CASCADE)


class PatientQuery(models.Model):
    queryId = AutoField(primary_key=True)
    queryDetails = TextField()
    patientId = ForeignKey(Patient, on_delete=models.CASCADE)


