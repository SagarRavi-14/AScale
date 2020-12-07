from django.db import models
import datetime
from datetime import date
# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    message = models.TextField()
    time_stamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    