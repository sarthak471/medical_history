from django.urls import path
from user_dashboard import views
from django.views.decorators.csrf import csrf_exempt
from user_dashboard import views

urlpatterns = [
    path('dashboard/',views.dashboardView,name = 'dashboard'),
]
