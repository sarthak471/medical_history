from django.shortcuts import render
from django.views import View



class Home(View):
    def get(self, request):
        return render(request,'landingpage/base.html')
    
# class About(View):
#     def get(self, request):
#         return render(request,'authentication/login.html')
    
# class Contact(View):
#     def get(self, request):
#         return render(request,'authentication/reset_password.html')
    