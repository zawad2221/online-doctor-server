from typing import Text
from django.db import models
from django.db.models.fields import AutoField, CharField, TextField
from django.db.models.fields.related import ForeignKey
from appointment.models import Appointment
from patient.models import Patient


class Suggestion(models.Model):
    suggestionId = AutoField(primary_key=True)
    suggestionDetails = TextField()

class PatientHistory(models.Model):
    patientHistoryId = AutoField(primary_key=True)
    patientHistoryDeatils = TextField()
    patientId = ForeignKey(Patient, on_delete=models.CASCADE)

class Prescription(models.Model):
    prescriptionId = AutoField(primary_key=True)
    appointmentId = ForeignKey(Appointment, blank=True, null=True, on_delete=models.CASCADE)
    suggestionId = ForeignKey(Suggestion, blank=True, null=True,on_delete=models.CASCADE)
    patientHistoryId = ForeignKey(PatientHistory, blank=True, null=True,on_delete=models.CASCADE)

class Company(models.Model):
    companyId = AutoField(primary_key=True)
    companyName = CharField(max_length=22)

class MedicineForm(models.Model):
    formId = AutoField(primary_key=True)
    formName = CharField(max_length=22)

class Medicine(models.Model):
    medicineId = AutoField(primary_key=True)
    medicineName = CharField(max_length=33)
    medicineFormId = ForeignKey(MedicineForm, on_delete=models.CASCADE)
    medicineCompanyId = ForeignKey(Company, on_delete=models.CASCADE)

class Instruction(models.Model):
    instructionId = AutoField(primary_key=True)
    instructionDetails = TextField()

class PrescribedMedicine(models.Model):
    prescribedMedicineId = AutoField(primary_key=True)
    prescriptionId = ForeignKey(Prescription, related_name='prescribed_medicine', on_delete=models.CASCADE)
    medicineId = ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = CharField(max_length=22)
    frequency = CharField(max_length=22)
    duration = CharField(max_length=22)
    instructionId = ForeignKey(Instruction, on_delete=models.CASCADE)