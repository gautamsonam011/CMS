# Here write your logical code
# This is a business logic layer 
from django.http import HttpResponse
from django.template import loader

def client_request_response(request):
    return HttpResponse("<h1>Hello Django Project</h1>")

def request_add_two_numbers(request):
    return HttpResponse("<h1>Add two numbers and sum = 78 </h1>")

def request_message(request):
    return HttpResponse("<h1>'Message type content' refers to either the actual data or text within a message (the content of the message) or, in a technical context, the definition of the structure and type of data a message can hold, such as MIME message types, SAP message types, or message types in programming languages like Java. The specific meaning depends on whether you're talking about the message's substance or its programmatic definition and structure. </h1>")

def my_first_template(request):
    template = loader.get_template('firstfile.html')