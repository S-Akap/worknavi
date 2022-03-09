from telnetlib import SE
from django.contrib import admin

# Register your models here.
from .models import Sex, Requirement, Citizenship, RegisteredStaff


class RegisteredStaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'age', 'requirement',
                    'hourly_pay', 'citizenship', 'residence', 'is_contact')


admin.site.register(Sex)
admin.site.register(Requirement)
admin.site.register(Citizenship)
admin.site.register(RegisteredStaff, RegisteredStaffAdmin)
