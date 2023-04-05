from django.urls import path
from user_dashboard import views
from django.views.decorators.csrf import csrf_exempt
from user_medical_profile import views

urlpatterns = [
    path('',views.MedicalDashboardView,name = 'usermedicaldashbaord'),
    path('usermedicaldashbaord/',views.MedicalDashboardView,name = 'usermedicaldashbaord'),
    # path('addmedicalreport/',views.AddReportView,name = 'addmedicalreport_noparameter'),
    path('addmedicalreport/<int:medical_condition_id>/<str:medical_condition_name>',views.AddReportView,name = 'addmedicalreport'),
    path('addmedicalcondition/',views.AddMedicalConditionView,name = 'addmedicalcondition'),
    path('editmedicalcondition/<int:medical_condition_id>',views.EditMedicalConditionView,name = 'editmedicalcondition'),
    path('viewallmedicalreport/<int:medical_condition_id>/<str:medical_condition_name>',views.ViewAllReportView,name = 'viewallmedicalreport'),
    path('viewmedicalreport/<int:report_id>/<str:medical_condition_name>',views.ViewReportView,name = 'viewmedicalreport'),
    path('deletemedicalcondition/<int:medical_condition_id>',views.DeleteMedicalCondtionView,name = 'deletemedicalcondition'),
    path('deletereport/<int:report_id>/<str:medical_condition_name>',views.DeleteReportView,name = 'deletereport'),
    path('editmedicalreport/<int:medical_condition_id>/<str:medical_condition_name>/<int:report_id>',views.EditReportView,name = 'editmedicalreport'),
]