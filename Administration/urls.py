from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.Administration, name="dashboard"),
    path('save-sidebar-setting/', views.save_sidebar_setting, name='save_sidebar_setting'),

    
]