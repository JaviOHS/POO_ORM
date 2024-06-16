from django.urls import include, path
from sga import views 
 
app_name='sga'

urlpatterns = [    
    path('', views.home, name='home'),
    
    path('periods/', views.period_list, name='period_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('students/', views.student_list, name='student_list'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('notes/', views.notes_list, name='notes_list'),
    path('notes_detail/', views.notes_detail_list, name='notes_detail_list'),
]