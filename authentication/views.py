from django.shortcuts import render,redirect
from django.views import View
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
import email_validator
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from email_validator import validate_email ,EmailNotValidError
from helper.helper import verifyemail ,genratelink ,validate_jwt
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import datetime
from django.contrib.auth.hashers import check_password
# Create your views here.


# SPECIAL_USE_DOMAIN_NAMES = ["@co"]
# email_validator.SPECIAL_USE_DOMAIN_NAMESSPECIAL_USE_DOMAIN_NAMES

class UsernameValidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']
        print("usernamevalidation")
        if not str(username).isalnum():
            return JsonResponse({"username_error":"the username should be alpha numeric"})
        if User.objects.filter(username = username).exists():
            return JsonResponse({'username_error':'sorry this username already exist'})
        return JsonResponse({'usernamevalid':True})

        # return render(request,'authentication/registor.html')

class EmailValidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        email = data['email']
        print("emailvalidation")
        try:
            v = validate_email(email)
            email = v["email"]
        except EmailNotValidError as e:
            print(str(e))
            return JsonResponse({"email_error":str(e)})
        if User.objects.filter(email = email).exists():
            return JsonResponse({'email_error':'sorry this email already exist'})
        return JsonResponse({'emailvalidation':True})

class RegistrationView(View):
    def get(self, request):
        return render(request,'authentication/registor.html')
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        if(username and password and email):
            try:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.is_active = False  
                user.save()
                link = genratelink(user_pk= user.pk)
                # verifyemail(email,link)
                print("==========",link)
                messages.success(request,'Your account has created successfully please click on link send to email to verify the your account')
                button_status = {
                            'back':True,
                            'resend':True,
                            'home':True,
                        }    
                response  = render(request,'authentication/activation.html',{'data':button_status})
                response.set_cookie('user_id', urlsafe_base64_encode(force_bytes(user.pk)) )
                response.set_cookie('email', urlsafe_base64_encode(force_bytes(email)) )  
                return response
            except Exception as e:
                print(e)
                messages.error(request,"something went wrong please try again")
        else:
            messages.error(request,"please fill all the fields")
        return render(request,'authentication/registor.html')
    

class LoginView(View):
    def get(self, request):
        return render(request,'authentication/login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        if(username and password):
            try:
                user = User.objects.get( username=username )
                if user == None and check_password(password,user.password):
                    messages.error(request,"Either the email or password is wrong")
                    return render(request,'authentication/login.html')
                else:
                    if check_password(password,user.password):
                        if user.is_active:
                            login(request,user)
                            return redirect('/dashboard/dashboard')
                        else:
                            messages.error(request,"The account is not verified")
                            return render(request,'authentication/login.html')
                    else:
                        messages.error(request,"Either the email or password is wrong")
                        return render(request,'authentication/login.html')
            except Exception as e:
                messages.error(request,"something went wrong please try again") 
                return render(request,'authentication/login.html')
        else:
            messages.error(request,"please fill all the fields")
        return render(request,'authentication/login.html')
    

class ResendValidationMail(View):
    def post(self,request):
        user_id = request.COOKIES['user_id']
        email = urlsafe_base64_decode(request.COOKIES['email'])
        user_obj = User.objects.get(pk = id)
        if(user_obj.is_active == True):
            messages.info(request,"Your account is already activated")
            button_status = {
                        'back':True,
                        'resend':False,
                        'home':True,
                    }
        else:
            link = genratelink(user_pk= user_id)
            verifyemail(email,link)
            button_status = {
                        'back':True,
                        'resend':True,
                        'home':True,
                    }        
        return render(request,'authentication/activation.html',{'data':button_status})

class ResetPasswordView(View):
    def get(self, request):
        data = json.loads(request.body)
        print(data)
        return render(request,'authentication/reset_password.html')
    
class SetNewPasswordView(View):
    def get(self, request):
        return render(request,'authentication/set_newpassword.html')
    
class LinkValidationView(View):
    def get(self,request,token):
        data = validate_jwt(token)
        status = data['status']
        id = data['id']
        if status:
            user_obj = User.objects.get(pk = id)
            if(user_obj.is_active == True):
                messages.info(request,"Your account is already activated")
            else:
                user_obj.is_active = True
                user_obj.save()
                messages.success(request,"Your account is activated kindly login")
            return render(request,'authentication/login.html')
        else:
            user_obj = User.objects.get(pk = id)
            messages.error(request,"The token is expired kindly rigister again again")
            button_status = {
                    'home':True,
                }
            return render(request,'authentication/activation.html',{'data':button_status})

    
class Acticationview(View):
    def get(self, request):
        button_status = {
                    'back':True,
                    'resend':True,
                    'home':True,
                }
        messages.success(request,'Your account has created successfully please click on link send to email to verify the your account')
        return render(request,'authentication/activation.html',{'data':button_status})
    

class Logoutview(View):
    def post(self, request):
        logout(request)
        messages.success(request,'You have been logout successfully')
        return redirect('login')