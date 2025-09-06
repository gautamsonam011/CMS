# Here write your logical code
# This is a business logic layer 
from django.http import HttpResponse
from django.shortcuts import render

def client_request_response(request):
    return HttpResponse("<h1>Hello Django Project</h1>")

def request_add_two_numbers(request):
    return HttpResponse("<h1>Add two numbers and sum = 78 </h1>")

def request_message(request):
    return HttpResponse("<h1>'Message type content' refers to either the actual data or text within a message (the content of the message) or, in a technical context, the definition of the structure and type of data a message can hold, such as MIME message types, SAP message types, or message types in programming languages like Java. The specific meaning depends on whether you're talking about the message's substance or its programmatic definition and structure. </h1>")

def my_first_template(request):
    return render(request, 'firstfile.html')

def my_home_page(request):
    return render(request, 'home.html')

def my_about_page(request):
    if request.method == "POST":
        print(request.POST)

        name = request.POST.get("name")
        d = {
            'name': name
        }
        return render(request, "about.html", context=d)

# def my_about_page(request):
    # if request.method == "POST":
    #     print(request.POST)

    #     name = request.POST.get("name")
    #     d = {
    #         'name': name
    #     }
    #     return render(request, "about.html", context=d)
    
    # # Handle GET request
    # return render(request, "about.html")        

def calculator_view(request):
    if request.method == "GET":
        resp = render(request, 'calculator.html')    
        return resp

    if request.method == "POST":
        pass    