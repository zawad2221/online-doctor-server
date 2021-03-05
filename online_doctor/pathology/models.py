from django.db import models
from django.db.models.fields import AutoField, CharField, DecimalField
from django.db.models.fields.related import ForeignKey
from chamber.models import Location
from custom_user.models import User

class Pathology(models.Model):
    pathologyId = AutoField(primary_key = True)
    pathologyLocationId = ForeignKey(Location, on_delete= models.CASCADE)
    pathologyUserId = ForeignKey(User, on_delete=models.CASCADE)

