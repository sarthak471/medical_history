from django.contrib import admin
from .models import MedicalCondition,Medicine,Report


# Register your models here.
admin.site.register(MedicalCondition)
admin.site.register(Medicine)
admin.site.register(Report)