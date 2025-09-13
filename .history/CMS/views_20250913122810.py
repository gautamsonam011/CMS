# Here write your logical code
# This is a business logic layer 
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from SDM.models import GroceryProducts
import json

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
    expression = ""
    result = ""

    if request.method == "POST":
        expression = request.POST.get("expression", "")

        if "btn" in request.POST:  
            expression += request.POST["btn"]

        elif "clear" in request.POST:  
            expression = ""
            result = ""

        elif "equal" in request.POST: 
            try:
                result = str(eval(expression))
                expression = result  
            except:
                result = "Error"
                expression = ""

    return render(request, "calculator.html", {"expression": expression, "result": result})

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


def create_view(request):
    if request.method == "POST":

        try:
            data = json.loads(request.body)

            grocery = GroceryProducts.objects.create(**data)

            return JsonResponse({
                'productName': grocery.productName,
                'brandName': grocery.brandName,
                'cost': grocery.cost,
                'price': grocery.price,
                'manu_date': grocery.manu_date,
                'exp_date': grocery.exp_date,

            }, status = 201)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    return JsonResponse({'error': 'Only POST method allowed'}, status = 405)    

# CRUD 
# Create query 

def save_product(request):
    if request.method == "POST":
        productName = request.POST.get('productName')
        brandName = request.POST.get('brandName')
        cost = request.POST.get('cost')
        price = request.POST.get('price')
        manu_date = request.POST.get('manu_date')
        exp_date = request.POST.get('exp_date')

        GroceryProducts.objects.create(
            productName = productName,
            brandName = brandName,
            cost = cost,
            price = price,
            manu_date = manu_date,
            exp_date = exp_date

        )
        
        return HttpResponse("Product saved successfully!")
    return render(request, 'products.html')

def update_product(request, product_id):
    if request.method == "POST":
        productName = request.POST.get('productName')
        brandName = request.POST.get('brandName')
        cost = request.POST.get('cost')
        price = request.POST.get('price')
        manu_date = request.POST.get('manu_date')
        exp_date = request.POST.get('exp_date')

        product = get_object_or_404(GroceryProducts, id = product_id)

        product.productName = productName
        product.brandName = brandName
        product.cost = cost
        product.price = price
        product.manu_date = manu_date
        product.exp_date = exp_date
      
        return HttpResponse("Product updated successfully!")
    product = get_object_or_404(GroceryProducts, id = product_id)
    return render(request, 'updateProduct.html', {'product':product})

def get_product(request):
    # products = GroceryProducts.objects.all()
    # products = Grocery
    products = GroceryProducts.objects.filter(productName='Milk')

    return render(request, 'getProduct.html',{'products':products})    




