from rest_framework import serializers
from .models import Doctor, Specialization
from custom_user.models import User
from chamber.serializers import RelatedFieldAlternative
from custom_user.serializers import CustomUserSerializer


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    doctorId = serializers.IntegerField(required=False)
    doctorSpecialization = RelatedFieldAlternative(queryset=Specialization.objects.all(), serializer=SpecializationSerializer, source='doctorSpecializationId')
    doctorUser = RelatedFieldAlternative(queryset=User.objects.all(), serializer=CustomUserSerializer, source = 'doctorUserId')
    class Meta:
        model = Doctor
        fields = ['doctorId','doctorBmdcId','doctorDesignation','doctorSpecialization','doctorUser']

    read_only_fields = ('doctorSpecialization','doctorUser')