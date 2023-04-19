from django.contrib import admin
from .models import MedicalCondition,Medicine,Report,MedicineImages,ReportImages


# Register your models here.
admin.site.register(MedicalCondition)
admin.site.register(Medicine)
admin.site.register(Report)
admin.site.register(ReportImages)
admin.site.register(MedicineImages)