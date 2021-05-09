from django.contrib import admin
from .models import Medicine, MedicineForm, Suggestion, Instruction, Company, Prescription, PrescribedMedicine, PatientHistory

admin.site.register(Medicine)
admin.site.register(MedicineForm)
admin.site.register(Suggestion)
admin.site.register(Instruction)
admin.site.register(Company)
admin.site.register(Prescription)
admin.site.register(PrescribedMedicine)
admin.site.register(PatientHistory)
