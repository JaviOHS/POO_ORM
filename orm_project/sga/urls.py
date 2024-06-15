from django.urls import include, path
from sga import views
 
app_name='sga'

urlpatterns = [    
    path('', views.home, name='home'),
]