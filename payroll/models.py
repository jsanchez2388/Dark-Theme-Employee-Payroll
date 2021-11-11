from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    middle_name = models.TextField()
    address = models.TextField()
    birth_date = models.DateField()
    email = EmailField(('email address'), unique=True)

class Employee(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    date_hired = models.DateField()
    pay_rate = models.FloatField()
    status = models.BooleanField()

    from django.db import models

class Paystub(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
    )
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    hours_worked = models.FloatField()
    deductions = models.FloatField()
    taxes = models.FloatField()
    total_compensation = models.FloatField()

class Schedule(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
    )
    mon_start = models.DateTimeField()
    mon_end = models.DateTimeField()
    tues_start = models.DateTimeField()
    tues_end = models.DateTimeField()
    wed_start = models.DateTimeField()
    wed_end = models.DateTimeField()
    thurs_start = models.DateTimeField()
    thurs_end = models.DateTimeField()
    fri_start = models.DateTimeField()
    fri_end = models.DateTimeField()
    sat_start = models.DateTimeField()
    sat_end = models.DateTimeField()
    sun_start = models.DateTimeField()
    sun_end = models.DateTimeField()