from django.urls import path
from authentication import views
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

 
urlpatterns = [
    # path('', views.RegistrationView.as_view(),name="registor"),
    path('registor/', views.RegistrationView.as_view(),name="registor"),
    path('login/', views.LoginView.as_view(),name="login"),
    path('logout/', views.Logoutview.as_view(),name="logout"),
    path('resetPassword/', views.ResetPasswordView.as_view(),name="resetPassword"),
    path('setNewPassword/', views.SetNewPasswordView.as_view(),name="setNewPassword"),
    path('activation/', views.Acticationview.as_view(),name="activation"), #this is to redirect to send email conformation and resend email page"""
    path('linkvalidate/<token>',views.LinkValidationView.as_view(),name="linkvalidate"),
    path('validateUsername/',views.UsernameValidationView.as_view(),name="validateUsername"),
    path('validateEmail/', views.EmailValidationView.as_view(),name="validateEmail"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
