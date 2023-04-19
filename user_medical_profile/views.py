from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import MedicalCondition ,Report ,Medicine ,ReportImages
from django.contrib import messages
import datetime
from django.utils.timezone import now
from django.core.paginator import Paginator , EmptyPage
from helper.helper import html_to_pdf
from django.http import HttpResponse



# def MedicalDashboardView(request):
#         print("i am in medical dashboard")
#         start = "None"
#         end = "None"
#         searchvalue = "None"
#         searchvalue = str(request.GET.get('searchvalue'))
#         searchvalue = "None" if searchvalue == "" else searchvalue
#         start = str(request.GET.get('start'))
#         start = str(request.GET.get('start'))
#         start = "None" if start ==  "" else start
#         end =  str(request.GET.get('end'))
#         end = str(request.GET.get('end'))
#         end = "None" if end == "" else end

#         print("filter  value ===============-------- ", searchvalue,start,end)
#         print("filter  value ===============-------- ", type(searchvalue),type(start),type(end))
#         if(start != "None" and end != "None" and searchvalue !="None" ):
#                 print("111111111111111111111111")
#                 filter_obj =  MedicalCondition.objects.filter(user_id = request.user).filter(date_of_start__range=[start, end]).filter(disease_name__icontains=searchvalue).values() | MedicalCondition.objects.filter(symptoms__icontains=searchvalue).values() | MedicalCondition.objects.filter(body_part_effected__icontains=searchvalue).values()
#                 filter_obj = filter_obj.distinct()
#         elif(start != "None" and end != "None" ):
#                 print("222222222222222222222222")
#                 filter_obj =  MedicalCondition.objects.filter(user_id = request.user).filter(date_of_start__range=[start, end])
#         elif( searchvalue != "None"):
#                 print("333333333333333333333")
#                 searchvalue = searchvalue
#                 filter_obj = MedicalCondition.objects.filter(user_id = request.user).filter(disease_name__icontains=searchvalue).values() | MedicalCondition.objects.filter(symptoms__icontains=searchvalue).values() | MedicalCondition.objects.filter(body_part_effected__icontains=searchvalue).values()
#                 filter_obj = filter_obj.distinct()
#         else:   
#                 print("4444444444444444444444")
#                 filter_obj = MedicalCondition.objects.filter(user_id = request.user)

#         print("filter ============= ",filter_obj)

#         p = Paginator(filter_obj,  1)
#         page_num = request.GET.get('page',1)
#         try:
#                 page = p.page(page_num)
#         except EmptyPage:
#                 page = p.page(1)
#         context = {
#                 'medical_condition_list':page,
#                 'searchvalue':searchvalue,
#                 'url':url

#         }
#         return render(request,'usermedicalprofile/medicalprofile.html',context)

def MedicalDashboardView(request):
        print("i am in medical dashboard")
        searchvalue =str(request.GET.get('searchvalue'))
        searchvalue = "None" if searchvalue == "" else searchvalue
        print("Search value == ",searchvalue)
        start = str(request.GET.get('start'))
        start = "None" if start ==  "" else start
        end =  str(request.GET.get('end'))
        end = "None" if end == "" else end
        print("start == ",start,end)
        if(start != "None" and end != "None" and searchvalue !="None" ):
                url=f"?searchvalue={searchvalue}&start={start}&end={end}&"              
                print("111111111111111111111111")
                filter_obj =  MedicalCondition.objects.filter(user_id = request.user).filter(date_of_start__range=[start, end])
                filter_obj = filter_obj.filter(disease_name__icontains=searchvalue).values() | filter_obj.filter(symptoms__icontains=searchvalue).values() | filter_obj.filter(body_part_effected__icontains=searchvalue).values()
                filter_obj = filter_obj.distinct()
        elif(start != "None" and end != "None" ):
                url=f"?start={start}&end={end}&"
                print("222222222222222222222222")
                filter_obj =  MedicalCondition.objects.filter(user_id = request.user).filter(date_of_start__range=[start, end])
        elif( searchvalue != "None"):
                print("333333333333333333333")
                url = f"?searchvalue={searchvalue}&"    
                searchvalue = searchvalue
                filter_obj = MedicalCondition.objects.filter(user_id = request.user).filter(disease_name__icontains=searchvalue).values() | MedicalCondition.objects.filter(symptoms__icontains=searchvalue).values() | MedicalCondition.objects.filter(body_part_effected__icontains=searchvalue).values()
                filter_obj = filter_obj.distinct()
        else:   
                url="?"
                print("4444444444444444444444")
                filter_obj = MedicalCondition.objects.filter(user_id = request.user)

        print("filter ============= ",filter_obj)

        page_num = request.GET.get('page',1)
        p = Paginator(filter_obj,  3)
        try:
                page = p.page(page_num)
        except EmptyPage:
                page = p.page(1)
        context = {
                'medical_condition_list':page,
                'searchvalue':searchvalue,
                'url':url,
                'start':start,
                'end':end
        }
        return render(request,'usermedicalprofile/medicalprofile.html',context)


def AddMedicalConditionView(request):
        print(request)
        if request.method == 'GET':

                return render(request,'usermedicalprofile/addmedicalcondition.html')
        
        if request.method == 'POST':

                print("i am in medical condition")
                disease_name = request.POST['disease_name']
                date_of_start = request.POST['date_of_start']
                symptoms = request.POST['symptoms']
                body_part_effected = request.POST['body_part_effected']

                if(len(date_of_start) == 0):
                        date_of_start = datetime.datetime.today().strftime('%Y-%m-%d')

                new_medical_condition = MedicalCondition.objects.create(user = request.user , 
                                                         disease_name = disease_name ,
                                                        date_of_start = date_of_start,symptoms=symptoms,body_part_effected = body_part_effected)
                new_medical_condition.save()
                messages.success(request,'Medical condition successfully')
        response = redirect('usermedicaldashbaord')  
        return response  

def EditMedicalConditionView(request,medical_condition_id):
        print("i am in edit EditMedicalConditionView ",medical_condition_id) 
        medical_condtion_data = MedicalCondition.objects.get(user_id = request.user , id = medical_condition_id)
        if request.method == 'GET':
                context = {
                        'medical_condtion_data':medical_condtion_data,
                        "date":str(medical_condtion_data.date_of_start)
                }

                return render(request,'usermedicalprofile/editmedicalcondition.html',context)
        
        if request.method == 'POST':

                print("i am in medical condition")
                disease_name = request.POST['disease_name']
                date_of_start = request.POST['date_of_start']
                symptoms = request.POST['symptoms']
                body_part_effected = request.POST['body_part_effected']

                medical_condtion_data.disease_name = disease_name
                medical_condtion_data.date_of_start = date_of_start
                medical_condtion_data.symptoms = symptoms
                medical_condtion_data.body_part_effected = body_part_effected
                medical_condtion_data.save()

                messages.success(request,'Medical condition updated successfully')
        response = redirect('usermedicaldashbaord')  
        return response  

def AddReportView(request,medical_condition_id ,medical_condition_name):
        print("i am in add report ")
        print(medical_condition_name)
        print(medical_condition_id)
        print(request.user.id)
        context = {
                'medicalconditionname':medical_condition_name,
                'medical_condition_id':medical_condition_id
        }

        if request.method == 'GET':
                return render(request,'usermedicalprofile/addreport.html',context)
        if request.method == 'POST':
                
                medical_condition_obj = MedicalCondition.objects.get(id = medical_condition_id)
                print("med================= ",medical_condition_obj)

                keyword = request.POST['keyword'] 
                doctor_name = request.POST['doctor_name']
                hospital_name = request.POST['hospital_name']
                hospital_phoneno = request.POST['hospital_phoneno']
                doctors_phoneno = request.POST['doctors_phoneno']
                hospital_address = request.POST['hospital_address']
                doctors_opinion = request.POST['doctors_opinion']
                symptoms = request.POST['symptoms']
                date_of_visit = request.POST['dob']                                                      

                print("value = =============== ",request.FILES )
                print("doctor name = ",doctor_name)       
                if(len(date_of_visit) == 0):
                        date_of_visit = datetime.datetime.today().strftime('%Y-%m-%d') 

                new_report_obj = Report.objects.create(user = request.user , 
                                        keyword = keyword,
                                        medical_condition_id = medical_condition_obj , 
                                        doctors_name = doctor_name,
                                        hospital_address = hospital_address , 
                                        hospital_name = hospital_name,
                                        hospital_phoneno = hospital_phoneno,
                                        doctors_phoneno = doctors_phoneno,
                                        doctors_option = doctors_opinion,
                                        symptoms = symptoms,            
                                        date_of_visit = date_of_visit)  
                new_report_obj.save()

                print("-------------------------------")
                medname = request.POST.getlist('medname')
                duration = request.POST.getlist('duration')
                interval = request.POST.getlist('interval')
                print(duration,interval,medname)

                for i in range(0,len(medname)):
                        if(medname[i] != "" and duration[i] != "" and interval[i] != "" ):
                                new_med_obj = Medicine.objects.create(user_id = request.user.id 
                                                                , medical_report_id_id = medical_condition_id ,
                                                                        report_id_id = new_report_obj.id,
                                                                        name = medname[i],
                                                                        duration = duration[i] , 
                                                                        interval = interval[i])
                                new_med_obj.save()                        
                print("----------------------------------")                
                # prescription_img = request.FILES.getlist('uploadimage')
                # print(prescription_img)
                # for i in prescription_img:
                #         print(" i = ",i)
                

                # for i in request.FILES.getlist['uploadimage']:
                #         print(" i =========== ",i)


                # print("the list is ======================== ",prescription_img)
                
                
                
                # if(len(prescription_img) != 0):
                #         for i in prescription_img:
                #                 new_report_image_obj = ReportImages.objects.create(report_id_id = new_report_obj.id,report_img = i)
                #                 new_report_image_obj.save()

                
                messages.success(request,'Report successfully added')
                return redirect('viewallmedicalreport', medical_condition_id=medical_condition_id,medical_condition_name=medical_condition_name)

def EditReportView(request,medical_condition_id,medical_condition_name,report_id):
        print("i am in edit report ")
        print(medical_condition_id)
        print(request.user.id)
        report_obj = Report.objects.get(id = report_id)
        print("report ========= ")
        print(report_id)
        context = {
                'report_obj' : report_obj,
                'medical_condition_name':medical_condition_name,
                'keyword':report_obj.keyword,
                'date_of_visit':str(report_obj.date_of_visit),
                'report_id':report_id
        }
        if request.method == 'GET':
                return render(request,'usermedicalprofile/editreport.html',context)
        if request.method == 'POST':
                keyword = request.POST['keyword']
                doctor_name = request.POST['doctor_name']
                hospital_name = request.POST['hospital_name']
                hospital_phoneno = request.POST['hospital_phoneno']
                doctors_phoneno = request.POST['doctors_phoneno']
                hospital_address = request.POST['hospital_address']
                doctors_opinion = request.POST['doctors_opinion']
                symptoms = request.POST['symptoms']
                date_of_visit = request.POST['dob']
                prescription_img = request.POST['uploadimage']

                if(len(date_of_visit) == 0):
                        date_of_visit = datetime.datetime.today().strftime('%Y-%m-%d') 
                report_obj.doctors_name = doctor_name
                report_obj.keyword = keyword
                report_obj.hospital_name = hospital_name
                report_obj.hospital_phoneno = hospital_phoneno
                report_obj.doctors_phoneno = doctors_phoneno
                report_obj.hospital_address = hospital_address
                report_obj.doctors_option = doctors_opinion
                report_obj.symptoms = symptoms
                report_obj.date_of_visit = date_of_visit
                report_obj.prescription_img = prescription_img
                report_obj.save()
                print("post req data ======== ",medical_condition_id,request.user.id)
                messages.success(request,'Report successfully updated')
                return redirect('viewallmedicalreport', medical_condition_id=medical_condition_id,medical_condition_name=medical_condition_name)


def ViewAllReportView(request,medical_condition_id,medical_condition_name):
        print("i am in view all report ")
        report_list = Report.objects.filter(user_id = request.user ,medical_condition_id = medical_condition_id)
        p = Paginator(report_list, 3)
        page_num = request.GET.get('page',1)
        try:
                page = p.page(page_num)
                
        except EmptyPage:
                page = p.page(1)
        context = {
                'report_list':page,
                'medicalcondtionname':medical_condition_name,
                'medicalconditionid':medical_condition_id,
        }
        print(report_list)
        return render(request,'usermedicalprofile/reportprofile.html',context)

def DeleteMedicalCondtionView(request,medical_condition_id):
        print("i am in delete medical condition ")
        instance = MedicalCondition.objects.get(id = medical_condition_id)      
        instance.delete()
        messages.success(request,'Medical condittion deleted successfully')
        return redirect('usermedicaldashbaord')  

def DeleteReportView(request,report_id,medical_condition_name):
        print("i am in delete reports condition ")
        instance = Report.objects.get(id = report_id)
        instance.delete()
        messages.success(request,'Report deleted successfully')
        return redirect('viewallmedicalreport', medical_condition_id=instance.medical_condition_id_id,medical_condition_name=medical_condition_name)


def ViewReportView(request,report_id,medical_condition_name):
        print("i am in view all report ")

        report_obj = Report.objects.get(id= report_id)
        report_img_obj = ReportImages.objects.filter(report_id_id= report_id)
        print(report_img_obj)
        context = {
                'report':report_obj,
                'medical_condition_name':medical_condition_name,
                'report_img_obj':report_img_obj,
        }
        print(report_obj)
        return render(request,'usermedicalprofile/viewreport.html',context)


def GenrateReportPdfView(request,report_id,medical_condition_name):
        print("i am in genrate dpffffffffffffffffffffffffff ")
        print(report_id)
        report_obj = Report.objects.get(id= report_id)
        context = {
                'report':report_obj,
                'medical_condition_name':medical_condition_name
        }
        pdf = html_to_pdf('usermedicalprofile/reportpdf.html',context)
        return HttpResponse(pdf, content_type='application/pdf')
