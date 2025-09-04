
from django.contrib import admin
from django.urls import path
from views import client_request_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path("client/", client_request_response), 
]
