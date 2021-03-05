from django.urls import path
from .views import patientRegistration

urlpatterns = [
    path('patientRegistration/', patientRegistration, name='patientRegistration'),
]
