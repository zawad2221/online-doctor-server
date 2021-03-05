from rest_framework import serializers
from .models import Patient
from custom_user.models import User
from chamber.serializers import RelatedFieldAlternative
from custom_user.serializers import CustomUserSerializer

class PatientSerializer(serializers.ModelSerializer):
    patientId = serializers.IntegerField(required=False)
    patientUser = RelatedFieldAlternative(queryset=User.objects.all(), serializer=CustomUserSerializer, source='patientUserId')

    class Meta:
        model = Patient
        fields = ['patientId','patientNid','patientGender','patientBloodGroup','patientDateOfBirth','patientUser']
    read_only_fields = ('patientUser')