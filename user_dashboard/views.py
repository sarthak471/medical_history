from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

# class Dashboard(View):
#     # @login_required(login_url='/authentication/login')
#     def get(self, request):
#         print(request)
#         return render(request,'dashboard/base.html')

@login_required() 
def dashboardView(request):
        print(request)
        return render(request,'dashboard/dashboard.html')



