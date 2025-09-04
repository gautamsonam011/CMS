
from django.contrib import admin
from django.urls import path
from django.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("client/", client_request ), 
]
