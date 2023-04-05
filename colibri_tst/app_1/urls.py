from django.urls import re_path
# from django.conf.urls import re_
from app_1 import views

# template tagging
app_name = "app_1"


urlpatterns = [    
    re_path(r'^relative', views.relative_path, name='relative_path'),
    re_path(r'^add_employee', views.add_employee, name='add_employee')
]
