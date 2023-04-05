from django.urls import path
from landingpage import views

urlpatterns = [
    path('', views.Home.as_view(),name="home"),
]
