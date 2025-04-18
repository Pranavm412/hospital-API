from django.db import models
from api.doctors.models import Doctor
from api.patients.models import Patient

class Mapping(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    assigned_at=models.DateTimeField(auto_now_add=True)