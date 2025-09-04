# Here write your logical code
# This is a business logic layer 
from django.http import HttpResponse

def client_request(request):
    return HttpResponse("<h1>Hello Django Project</h1>")
