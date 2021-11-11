from django.db import models
from django.db.models.fields import DateField, EmailField

# Create your models here.
class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    middle_name = models.CharField()
    address = models.CharField()
    birth_date = models.DateField()
    email = EmailField(('email address'), unique=True)


