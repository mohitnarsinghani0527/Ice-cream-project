from django.shortcuts import render
from django.http import HttpResponse
from.models import customer
def demo(request):
    return render('hello')

def cus_data(request):
    return render(request,'index.html')


def cus_res(request):
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
   
    # ...

    # Check if 'contact_no' exists in the request data


    dbs=customer(name=name,email=email,password=password)
    dbs.save()
    # return HttpResponse('successfully done ')
    return render(request,'mohit.html')

# Create your views here.