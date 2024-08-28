from django.db import models
from django.utils import timezone
# Create your models here.


class Binnacle(models.Model):

    timestamp = models.DateTimeField(default=timezone.now)
    level = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.message}"