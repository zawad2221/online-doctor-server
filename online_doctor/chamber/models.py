from django.db import models
from django.db.models.fields import AutoField, CharField, DecimalField
from django.db.models.fields.related import ForeignKey
from custom_user.models import User

class Location(models.Model):
    locationId = AutoField(primary_key=True)
    locationAdderssDetail = CharField(max_length=55)
    locationLongitude = DecimalField(max_digits=33, decimal_places= 22)
    locationLatitude = DecimalField(max_digits=33, decimal_places= 22)


class Chamber(models.Model):
    chamberId = AutoField(primary_key= True)
    chamberLocationId = ForeignKey(Location, on_delete= models.CASCADE)
    chamberUserId = ForeignKey(User, on_delete=models.CASCADE)
