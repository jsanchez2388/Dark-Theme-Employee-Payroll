from django.db import models
from django.db.models.fields import DateField, EmailField

# Create your models here.
class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    middle_name = models.TextField()
    address = models.TextField()
    birth_date = models.DateField()
    email = EmailField(('email address'), unique=True)


