from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('admincreation',AdminView.as_view()),
    path('adminlogin',AdminLogin.as_view()),
    path('scheme',SchemeView.as_view()),
    path('scheme_category',SchemeCategoryView.as_view())    
    
]
