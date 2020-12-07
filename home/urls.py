from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('analytics/',views.analytics,name='analytics'),
    path('logout/',views.handleLogout, name='handleLogout'),
    
]

