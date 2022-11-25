from django.db import models

class Patient(models.Model):
    patient_id=models.CharField(max_length=25)
    name = models.CharField(max_length=75)
    consulting_doc = models.CharField(max_length=75)
    disease_details = models.TextField(null=True, blank=True)

    def __str__(self):
            return self.name

class Medicine(models.Model):
    patient_id = models.CharField(max_length=25)
    name = models.CharField(max_length=75)
    morning=models.BooleanField()
    afternoon=models.BooleanField()
    night=models.BooleanField()

    def __str__(self):
            return self.name
