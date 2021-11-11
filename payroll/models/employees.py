from django.db import models

from payroll.models.persons import Person

# Create your models here.
class Employee(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    date_hired = models.DateField
    pay_rate = models.FloatField()
    status = models.BooleanField()