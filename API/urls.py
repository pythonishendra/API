from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('admincreation',AdminView.as_view()),
    path('adminlogin',AdminLogin.as_view()),
    path('scheme',SchemeView.as_view()),
    path('scheme_category',SchemeCategoryView.as_view())  ,
    path('all_scheme_category',GetAllSchemeCategoryView.as_view()) ,
    path('all_centered_scheme',GetAllCenterSchemeView.as_view()) ,
    path('center_scheme_on_category',GetAllCenterSchemeBasedonCategoryView.as_view()),
    path('state_schemes',GetAllSchemesBasedOnStateView.as_view()),
    #path('scheme_with_detail',GetSchemesWithDetailView.as_view()),
    path('get_schemes_based_on_user',GetSchemesBasedOnUserView.as_view())
    
]
