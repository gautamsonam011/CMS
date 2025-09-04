
from django.contrib import admin
from django.urls import path
from django.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("client/", views.client_request.as_view()), 
]
