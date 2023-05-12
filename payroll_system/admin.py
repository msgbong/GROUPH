from django.contrib import admin
from .models import Employee, TeachingStaff, NonTeachingStaff, User, Payroll

admin.site.register(Employee)
admin.site.register(TeachingStaff)
admin.site.register(NonTeachingStaff)
admin.site.register(User)
admin.site.register(Payroll)
