from email.policy import default
from django.db import models
from datetime import datetime
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(defaults="")
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(default=datetime.now(), blank=True)

# Create your models here.
