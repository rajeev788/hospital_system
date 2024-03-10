


from django.db import models
from staffandpatient.models import Patient
from django.utils import timezone
import random
import string
from uuid import uuid4

SERVICE_TYPES = [
        ('Consultation', 'Consultation'),
        ('X-Ray', 'X-Ray'),
        ('Blood Test', 'Blood Test'),
        ('Admit','Admit'),
        ('Medications','Medications')
]

class Invoice(models.Model):
   
    invoice_date = models.DateField(default=timezone.now)
    patient_name = models.ForeignKey(Patient,on_delete=models.CASCADE)
    invoice_number = models.UUIDField(default = uuid4 ,editable = False)

    def __str__(self):
        return f"Invoice {self.invoice_number}"
   

class Service(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service_name=models.CharField(max_length=200,choices=SERVICE_TYPES)
    description = models.CharField(max_length=200,null=True,blank=True)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


   
    