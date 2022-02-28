from django.contrib import admin

# Register your models here.
from .models import RegisteredStaff


class RegisteredStaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'age', 'requirement',
                    'hourly_pay', 'citizenship', 'residence', 'is_contact')


admin.site.register(RegisteredStaff, RegisteredStaffAdmin)
