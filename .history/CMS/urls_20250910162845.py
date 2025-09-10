
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("client/", views.client_request_response), 
    path("add/", views.request_add_two_numbers),
    path('message/', views.request_message),
    path('first/', views.my_first_template),
    path('home/', views.my_home_page),
    path('about/', views.my_about_page),
    path('calculator/', views.calculator_view),
    path('dtl/', views.dtl_func),
    path('postapi/', views.create_view),
    path('create/', views.save_product)
]
