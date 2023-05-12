from django.db import models
from django.utils import timezone

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

MARITAL_STATUS_CHOICES = [
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
]

STAFF_TYPE_CHOICES = [
    ('teaching', 'Teaching Staff'),
    ('non_teaching', 'Non-Teaching Staff'),
]


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    marital_status = models.CharField(
        max_length=20, choices=MARITAL_STATUS_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    nationality = models.CharField(max_length=100)
    staff_type = models.CharField(max_length=20, choices=STAFF_TYPE_CHOICES)
    bank_account_number = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# compute.html related starts.


class Employee(models.Model):
    surname = models.CharField(max_length=50)
    othername = models.CharField(max_length=50)
    staff_type = models.CharField(max_length=20, choices=[
        ('teaching', 'Teaching Staff'),
        ('non-teaching', 'Non-Teaching Staff')
    ])

    def __str__(self):
        return f"{self.surname}, {self.othername}"


class TeachingStaff(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    housing_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    gross_pay = models.DecimalField(max_digits=10, decimal_places=2)
    payee = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.employee)


class NonTeachingStaff(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    medical_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.employee)


class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    gross_pay = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    payee = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    net_pay = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.employee)
