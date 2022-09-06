from django.db import models
import uuid

# Create your models here.
class Registration(models.Model):
    registration_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name_patient = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    date = models.DateTimeField()
    name_doctor = models.CharField(max_length=100)
    def __str__(self):
        return self.name_patient