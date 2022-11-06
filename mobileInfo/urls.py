
from django.contrib import admin
from django.urls import path
from django.urls import include
from mobileInfo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('info',views.info,name='information')
]
