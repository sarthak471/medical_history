from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# Create your models here.
class MedicalCondition(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    date_of_added = models.DateField(default=now)
    disease_name = models.CharField(max_length=255,blank=False)
    date_of_start = models.DateField(null=True)
    symptoms = models.TextField(null=True)
    body_part_effected = models.TextField(null=True)

    def __str__(self):
        return f'{self.disease_name}__{self.user}'
    
class Report(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    medical_condition_id = models.ForeignKey(to=MedicalCondition,on_delete=models.CASCADE)
    
    keyword = models.CharField(max_length=255,blank=True,null=True)
    doctors_name = models.CharField(max_length=255,blank=True,null=True)
    hospital_name = models.CharField(max_length=255,blank=True,null=True)

    hospital_phoneno = models.IntegerField(blank=True, null=True  )
    doctors_phoneno = models.IntegerField(blank=True, null=True   )

    hospital_address = models.CharField(max_length=255,blank=True ,null=True)
    doctors_option = models.TextField(blank=True ,null=True)

    symptoms = models.TextField(blank=True ,null=True)
    body_part_effected = models.TextField(blank=True ,null=True)

    date_of_visit = models.DateField(default=now)

    prescription_img = models.ImageField(null=True , blank=True) 
      
    def __str__(self):
        return f'{self.doctors_name}__'
    

class Medicine(models.Model):

    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    medical_report_id = models.ForeignKey(to=MedicalCondition,on_delete=models.CASCADE)
    report_id = models.ForeignKey(to=Report,on_delete=models.CASCADE)

    name = models.CharField(max_length=255,blank=True,null=True)
    duration = models.IntegerField(blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)

    medicine_img = models.ImageField(null=True)
   
    def __str__(self):
        return f'{self.name}__'

class MedicineImages(models.Model):

    medicine_id = models.ForeignKey(to=Medicine,on_delete=models.CASCADE)
    medicine_img = models.ImageField(null=True)
   
    def __str__(self):
        return f'{self.medicine_id}__'
    
class ReportImages(models.Model):

    report_id = models.ForeignKey(to=Report,on_delete=models.CASCADE)
    report_img = models.ImageField(null=True,blank=True,upload_to="newimages")
   
    def __str__(self):
        return f'{self.report_id}__'



    # wieght 
    # height
    # blood gropu
    # bmi#
    # eyes sight
    # plateltates
    # phylicl siablitites