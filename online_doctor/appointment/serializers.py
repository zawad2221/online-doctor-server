from custom_user.serializers import RelatedFieldAlternative
from rest_framework import serializers
from .models import Appointment
from visiting_schedule.models import VisitingSchedule
from patient.models import Patient
from visiting_schedule.serializers import VisitingScheduleSerializer
from patient.serializers import PatientSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    appointmentVisitingSchedule = RelatedFieldAlternative(
        queryset=VisitingSchedule.objects.all(), 
        serializer = VisitingScheduleSerializer,
        source = 'appointmentVisitingScheduleId',
        )
    appointmentPatient = RelatedFieldAlternative(
        queryset=Patient.objects.all(), 
        serializer = PatientSerializer,
        source = 'appointmentPatientId'
        )
    patientSymptomNote = serializers.CharField(allow_blank=True,source = 'appointmentPatientSymptomNote')
    class Meta: 
        model = Appointment
        fields = [
            'appointmentId',
            'appointmentPaymentCredential',
            'patientSymptomNote',
            'appointmentTime',
            'appointmentIsConfirmed',
            'appointmentIsCanceled',
            'appointmentIsVisited',
            'appointmentDate',
            'appointmentSerialNumber',
            'appointmentVisitingSchedule',
            'appointmentPatient',
            'appointmentType'
            ]
        
        