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
    res = ""
    if request.method == "POST":
        for i in range(10):  
            btn = f"btn{i}"
            if btn in request.POST:
                res = str(i)

        if 'btnsum' in request.POST:
            res = "+"
        elif 'btnsub' in request.POST:
            res = "-"
        elif 'btnmult' in request.POST:
            res = "*"
        elif 'btndiv' in request.POST:
            res = "/"
        elif 'btnmod' in request.POST:
            res = "%"

    return render(request, "calculator.html", {"res": res})


def dtl_func(request):
    a = 67
    b = 87
    sum = a+b
    l = ["Python", "Java", "PHP", "C#","HTML"]
    
    student_name = ["Ram", "Ankit", "Raj", "Geeta", "Rita"] 
    student_age = [14, 13, 15, 16, 14]  
    student_address = ["Delhi", "Kanpur", "Pune", "Mumbai", "Kolkata"] 

    students = zip(student_name, student_age, student_address)
    d = {
        'sum':sum,
        'techno': l,
        'students': students,
        }
    return render(request, 'dtl.html', d)



