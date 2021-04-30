from django.db import models
from django.db.models.fields import AutoField, CharField, DecimalField, TextField
from django.db.models.fields.related import ForeignKey
from custom_user.models import User
from patient.models import PatientQuery

class Location(models.Model):
    locationId = AutoField(primary_key=True)
    locationAdderssDetail = CharField(max_length=55)
    locationLongitude = DecimalField(max_digits=33, decimal_places= 22)
    locationLatitude = DecimalField(max_digits=33, decimal_places= 22)


class Chamber(models.Model):
    chamberId = AutoField(primary_key= True)
    chamberLocationId = ForeignKey(Location, on_delete= models.CASCADE)
    chamberUserId = ForeignKey(User, on_delete=models.CASCADE)

class AskedQuery(models.Model):
    askedQueryId = AutoField(primary_key=True)
    askedQueryAnswer = TextField(blank=True)
    chamberId = ForeignKey(Chamber, on_delete=models.CASCADE)
    queryId = ForeignKey(PatientQuery, on_delete=models.CASCADE)
