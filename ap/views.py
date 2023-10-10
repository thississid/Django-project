from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import OrderForm

def home(request):
    return render(request,'home.html',{'name':'Siddartha'})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{'result':res})

def dashboard(request):
    customers=Customer.objects.all()
    ord=Order.objects.all()
    return render(request,'dashboard.html',{'customers':customers, 'ord':ord})

def products(request):
    product=Product.objects.all()
    return render(request,'products.html',{'p':product})

def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    customers=Customer.objects.all()

    orders=customer.order_set.all()
    order_count=orders.count()

    context={'customers':customers, 'cust':customer,'ord':orders,'ordcount':order_count}

    return render(request, 'customer.html', context)

def createOrder(request):
    form = OrderForm()

    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}

    return render(request,'order_form.html',context)

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=="POST":
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'order_form.html',context)

def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)

    if request.method=="POST":
        order.delete()
        return redirect("/")

    context={'item':order}

    return render(request,'delete.html',context)