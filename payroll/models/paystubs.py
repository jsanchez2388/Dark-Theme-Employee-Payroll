from django.db import models

from payroll.models.employees import Employee

# Create your models here.
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