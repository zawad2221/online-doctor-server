from django.db import models
from django.db.models.fields import AutoField, BooleanField, CharField, FloatField, IntegerField, TextField, TimeField
from django.db.models.fields.related import ForeignKey
from rest_framework import serializers

from doctor.models import Doctor
from chamber.models import Chamber


class DaysOfWeek(models.Model):
    DAYS = (
        ("saturday","saturday"),
        ("sunday","sunday"),
        ("monday","monday"),
        ("tuesday","tuesday"),
        ("wednesday","wednesday"),
        ("thursday","thursday"),
        ("friday","friday")

    )
    datsOfWeekId = AutoField(primary_key=True)
    day = CharField(max_length= 10, choices = DAYS, unique=True)

    def __str__(self):
        return self.day

class Fee(models.Model):
    feeId = AutoField(primary_key= True)
    oldFee = IntegerField()
    newFee = IntegerField()
    reportFee = IntegerField()

    def __int__(self):
        return self.feeId

class VisitingSchedule(models.Model):
    visitingScheduleId = AutoField(primary_key=True)
    startAt = TimeField()
    endAt = TimeField()
    maxPatient = IntegerField()
    isCanceled = BooleanField(default=False)
    isDeleted = BooleanField(default=False)
    visitingScheduleFeeId = ForeignKey(Fee, on_delete= models.CASCADE)
    visitingScheduleDaysOfWeekId = ForeignKey(DaysOfWeek, on_delete= models.CASCADE)
    visitingScheduleDoctorId = ForeignKey(Doctor, on_delete= models.CASCADE)
    visitingScheduleChamberId = ForeignKey(Chamber, on_delete=models.CASCADE)
    visitingScheduleAdditionalInformation = TextField()


