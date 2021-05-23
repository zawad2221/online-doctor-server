from django.db.models import fields
from .models import Test, TestReport, TestType
from rest_framework import serializers
from pathology.models import Pathology
from pathology.serializers import PathologySerializer
from prescription.models import Prescription
from prescription.serializers import PrescriptionSerializer
from custom_user.serializers import RelatedFieldAlternative

class TestTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestType
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    testType = RelatedFieldAlternative(queryset=TestType.objects.all(),serializer=TestTypeSerializer, source='typeId')
    pathologyCenter = RelatedFieldAlternative(queryset=Pathology.objects.all(),serializer=PathologySerializer, source='pathologyId')
    class Meta:
        model = Test
        fields = ['testId','testRate','testType','pathologyCenter']

class TestReportSerializer(serializers.ModelSerializer):
    prescription = RelatedFieldAlternative(queryset=Prescription.objects.all(),serializer=PrescriptionSerializer, source='prescriptionId')
    test = RelatedFieldAlternative(queryset=Test.objects.all(),serializer=TestSerializer, source='testId')
    testType = RelatedFieldAlternative(queryset=TestType.objects.all(),serializer=TestTypeSerializer, source='typeId')

    class Meta:
        model=TestReport
        fields=[
            'testReportId', 
            'testReportDetails', 
            'issueDate', 
            'isDone', 
            'filePath',  
            'prescription', 
            'test',
            'testType'
        ]
    depth=1