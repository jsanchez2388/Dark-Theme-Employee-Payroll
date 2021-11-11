from django.db import models

from payroll.models.employees import Employee

# Create your models here.
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