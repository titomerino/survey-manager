from django.contrib import admin
from django.urls import path, include  

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('survey/', include('survey.urls')),
    path('student/', include('student.urls')),
    path('profile/', views.update_profile_view, name='profile'),
]
