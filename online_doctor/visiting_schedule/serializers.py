from django.db import models
from rest_framework import serializers

from .models import Fee, DaysOfWeek, VisitingSchedule
from custom_user.serializers import RelatedFieldAlternative
from doctor.models import Doctor
from chamber.models import Chamber
from doctor.serializers import DoctorSerializer
from chamber.serializers import ChamberSerializer

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'


class DaysOfWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaysOfWeek
        fields = '__all__'

class VisitingScheduleSerializer(serializers.ModelSerializer):
    visitingScheduleFee = RelatedFieldAlternative(
        queryset = Fee.objects.all(), 
        serializer = FeeSerializer, 
        source = 'visitingScheduleFeeId'
        )
    visitingScheduleDaysOfWeek = RelatedFieldAlternative(
        queryset = DaysOfWeek.objects.all(), 
        serializer = DaysOfWeekSerializer, 
        source = 'visitingScheduleDaysOfWeekId'
        )
    visitingScheduleDoctor = RelatedFieldAlternative(
        queryset = Doctor.objects.all(), 
        serializer = DoctorSerializer, 
        source = 'visitingScheduleDoctorId'
        )
    visitingScheduleChamber = RelatedFieldAlternative(
        queryset = Chamber.objects.all(), 
        serializer = ChamberSerializer, 
        source = 'visitingScheduleChamberId'
        )
    class Meta:
        model = VisitingSchedule
        fields = [
            "visitingScheduleId", 
            "startAt", 
            "endAt", 
            "maxPatient", 
            "isCanceled", 
            "isDeleted", 
            "visitingScheduleFee", 
            "visitingScheduleDaysOfWeek", 
            "visitingScheduleDoctor", 
            "visitingScheduleChamber",
            "visitingScheduleAdditionalInformation"
            ]
            


    