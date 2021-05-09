from django.db import models
from django.db.models import fields
from rest_framework import serializers
from custom_user.serializers import RelatedFieldAlternative
from appointment.serializers import AppointmentSerializer
from appointment.models import Appointment
from .models import Medicine, MedicineForm, Suggestion, Instruction, Company, Prescription, PrescribedMedicine, PatientHistory

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class MedicineFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineForm
        fields = '__all__'

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'

class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = '__all__'

class PatientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    # medicineForm = RelatedFieldAlternative(queryset=MedicineForm.objects.all(), serializer=MedicineFormSerializer,source='medicineFormId')
    # medicineCompany = RelatedFieldAlternative(queryset=Company.objects.all(), serializer=CompanySerializer,source='medicineCompanyId')
    medicineForm = MedicineFormSerializer(many=False, source='medicineFormId')
    medicineCompany = CompanySerializer(many=False, source='medicineCompanyId')
    class Meta:
        model = Medicine
        fields = ['medicineId', 'medicineName', 'medicineForm', 'medicineCompany']
    def create(self, validated_data):
        medicineFormData=validated_data.pop('medicineFormId')
        medicineForm, medicineFormCreate = MedicineForm.objects.get_or_create(**medicineFormData)
        # if medicineFormCreate==True:
        #     medicineForm = medicineFormCreate
        medicineCompanyData=validated_data.pop('medicineCompanyId')
        medicineCompany, medicineCompanyCreate = Company.objects.get_or_create(**medicineCompanyData)
        # if medicineCompanyCreate==True:
        #     medicineCompany = medicineCompanyCreate
        medicine = Medicine.objects.create(medicineFormId=medicineForm,medicineCompanyId=medicineCompany,**validated_data)

        return medicine

class PrescribedMedicineSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(many=False, source='medicineId')
    instruction = InstructionSerializer(many=False, source='instructionId')
    class Meta:
        model = PrescribedMedicine
        fields = ['prescribedMedicineId', 'medicine', 'quantity', 'frequency', 'duration', 'instruction']
    # def create(self, validated_data):
    #     instructin_data = validated_data.pop('instructionId')
    #     instruction = Instruction.objects.create(**instructin_data)
    #     medicine_data = validated_data.pop('medicineId')
    #     medicine, create_medicine = Medicine.objects.get_or_create(**medicine_data)
    #     print("medicine get ",medicine)
    #     if create_medicine==True:
    #         print("medicine create")
    #         medicine = create_medicine
    #     prescribedMedicine = PrescribedMedicine.objects.create(medicineId=medicine, instructionId=instruction, **validated_data)
    #     return prescribedMedicine


class PrescriptionSerializer(serializers.ModelSerializer):
    prescribedMedicine = PrescribedMedicineSerializer(many=True,source='prescribed_medicine')
    #appointment = RelatedFieldAlternative(queryset=Appointment.objects.all(), serializer=AppointmentSerializer, source='appointmentId')
    appointment=AppointmentSerializer(many=False, source='appointmentId')
    ##appointment = serializers.PrimaryKeyRelatedField(source='appointmentId')
    suggestion = SuggestionSerializer(many=False, source='suggestionId')
    patientHistory = PatientHistorySerializer(many=False, source='patientHistoryId')
    
    class Meta:
        model = Prescription
        fields = ['prescriptionId', 'appointment', 'suggestion', 'patientHistory','prescribedMedicine']
        #depth=1
    def create(self, validated_data):
        prescribed_medicines_data = validated_data.pop('prescribed_medicine')
        suggestion_data = validated_data.pop('suggestionId')
        patient_history_data = validated_data.pop('patientHistoryId')
        patientHistory = PatientHistory.objects.create(**patient_history_data)
        suggestion = Suggestion.objects.create(**suggestion_data)
        appointment_data=validated_data.pop('appointmentId')
        appointment, create = Appointment.objects.get_or_create(**appointment_data)
        if create==True:
            appointment=create
        print("got appointment: ", appointment)
        prescription = Prescription.objects.create(appointmentId=appointment, patientHistoryId=patientHistory, suggestionId=suggestion, **validated_data)
        print("create prescription: ", prescription)
        for prescribed_medicine_data in prescribed_medicines_data:
            instructin_data = prescribed_medicine_data.pop('instructionId')
            instruction = Instruction.objects.create(**instructin_data)
            medicine_data = prescribed_medicine_data.pop('medicineId')
            medicineFormData=medicine_data.pop('medicineFormId')
            medicineForm, medicineFormCreate = MedicineForm.objects.get_or_create(**medicineFormData)
            # if medicineFormCreate==True:
            #     medicineForm = medicineFormCreate
            medicineCompanyData=medicine_data.pop('medicineCompanyId')
            medicineCompany, medicineCompanyCreate = Company.objects.get_or_create(**medicineCompanyData)
            # if medicineCompanyCreate==True:
            #     medicineCompany = medicineCompanyCreate
            medicine, create_medicine = Medicine.objects.get_or_create(medicineFormId=medicineForm,medicineCompanyId=medicineCompany,**medicine_data)
            # if create_medicine==True:
            #     medicine=create_medicine
            print("medicine get ",medicine)
            if create_medicine==True:
                print("medicine create")
                medicine = create_medicine
            PrescribedMedicine.objects.create(prescriptionId=prescription, medicineId=medicine, instructionId=instruction, **prescribed_medicine_data)
            print("create prescribed medicine")
        return prescription
        