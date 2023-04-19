from django.urls import path
from user_profile import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.profileView,name='profile'),
    path('profile/',views.profileView,name='profile'),
    path('editprofile/',views.editProfileView,name='editprofile'),
    path('addprofile/',views.addProfileView,name='addprofile'),
]
