from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import UserGenralProfile
import datetime
from django.contrib import messages

@login_required() 
def profileView(request):
        print(request)
        return render(request,'userprofile/profile.html')


@login_required() 
def editProfileView(request): 
        exist = UserGenralProfile.objects.filter(user  = request.user)
        user_obj = None
        if exist:
                user_obj = UserGenralProfile.objects.get(user = request.user) 
                print("=================",user_obj.dob)
        if request.method == 'GET':
                user_detail_list = {}
                if user_obj:
                        d = str(datetime.date(user_obj.dob.year, user_obj.dob.month, user_obj.dob.day))
                        user_detail_list = {'firstname' : user_obj.first_name,
                                            'lastname':user_obj.last_name,
                                            'dob': d,
                                            'address': user_obj.address,
                                            'phoneno':user_obj.phone_number,
                                                }
                        return render(request,'userprofile/editprofile.html',{'user_detail_list':user_detail_list})
                return render(request,'userprofile/editprofile.html',{'user_detail_list':None})
        if request.method == 'POST':
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                dob = request.POST['dob']
                address = request.POST['address']
                phoneno = request.POST['phoneno']
                user_detail_list = {'firstname' : firstname,
                                            'lastname':lastname,
                                            'dob': dob,
                                            'address':address,
                                            'phoneno':phoneno
                                                }
                if user_obj:
                        user_obj.first_name = firstname
                        user_obj.last_name = lastname
                        user_obj.dob = dob
                        user_obj.address = address
                        user_obj.profile_img = None
                        user_obj.phone_number=phoneno
                        if 'image' in request.FILES:
                                user_obj.profile_img = request.FILES['uploadimage']
                        print("=======================================",request.FILES['uploadimage'])
                        user_obj.save()
                        messages.success(request,'Your genral profile updated successfully'     )
                else:
                        new_user_obj = UserGenralProfile.objects.create(user = request.user , 
                                                         first_name = firstname , last_name= lastname,dob = dob,address=address,profile_img = request.FILES['uploadimage'],phone_number = phoneno)
                
                        new_user_obj.save()
                        messages.success(request,'Your genral profile created successfully')
                return render(request,'userprofile/editprofile.html',{'user_detail_list':user_detail_list})



