
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from app_1 import views

urlpatterns = [    
    re_path(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('app_1/', include('app_1.urls'))
]
