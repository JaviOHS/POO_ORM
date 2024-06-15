from django.contrib import admin
from django.urls import path, include
from sga import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    path('sga/', include('sga.urls', namespace='sga')),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
