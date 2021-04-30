from rest_framework import serializers
from .models import Patient, PatientQuery
from custom_user.models import User
from custom_user.serializers import CustomUserSerializer, RelatedFieldAlternative

class PatientSerializer(serializers.ModelSerializer):
    patientId = serializers.IntegerField(required=False)
    patientUser = RelatedFieldAlternative(queryset=User.objects.all(), serializer=CustomUserSerializer, source='patientUserId')

    class Meta:
        model = Patient
        fields = ['patientId','patientNid','patientGender','patientBloodGroup','patientDateOfBirth','patientUser']
    read_only_fields = ('patientUser')

class PatientQuerySerializer(serializers.ModelSerializer):
    patient = RelatedFieldAlternative(queryset=Patient.objects.all(), serializer=PatientSerializer,source='patientId')
    class Meta:
        model = PatientQuery
        fields =['queryId','queryDetails','patient']