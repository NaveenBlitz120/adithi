from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import Create , Update , Update_order
from order.models import product , orders , orderedcart
from .filters import myFilter , orderFilter
from .decorators import allowed_user ,unauthenticated_user


st='/admin'
# Create your views here.
@allowed_user(allowed_roles=['admin'])
def home(request):
    order = orders.objects.all()
    products = product.objects.all()
    total_products = products.count()
    total_orders = order.count()
    completed = order.filter(status='completed').count()
    pending = order.filter(status='pending').count()

    orderfil = orderFilter(request.GET , queryset=order)
    order = orderfil.qs

    context = {'orders':order, 'products':products,
    'total_orders':total_orders,'completed':completed,
	'pending':pending ,'filter':orderfil }
    return render(request, 'admin/dashboard.html', context)

@allowed_user(allowed_roles=['admin'])
def stock(request):
    prod_obj = product.objects.all()
    myfilter = myFilter(request.GET,queryset=prod_obj)
    prod_obj= myfilter.qs    
    context ={ 'prod':prod_obj , 'filter':myfilter  }
    print(prod_obj ,context['prod'])
    return render(request, 'admin/search.html',context)


@allowed_user(allowed_roles=['admin'])
def create(request):
    
    form = Create()
    context = {'form':form,}
    if request.method == 'POST':
        #print('printing POST:',request.POST)
        form = Create(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect(st)

    return render(request,'admin/forms.html',context)

@allowed_user(allowed_roles=['admin'])
def success(request):
    return HttpResponse('your task completed successfully')

@allowed_user(allowed_roles=['admin'])
def update(request,pk):
    
    order = product.objects.get(id=pk)
    form = Update(instance=order)
    if request.method == 'POST':
        form = Update(request.POST,instance = order)
        if form.is_valid():
            form.save()
            return redirect(st)


    context = {'form':form}
    return render(request,'admin/forms.html',context)

@allowed_user(allowed_roles=['admin'])
def delete(request,pk):
    
    order = product.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect(st)

    context = {'item':order}
    return render(request,'admin/delete.html',context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'admin/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def update_order(request , pk):
    order = orders.objects.get(id=pk)
    form = Update_order(instance=order)
    if request.method == 'POST':
        form = Update_order(request.POST,instance = order)
        if form.is_valid():
            form.save()
            return redirect(st)

    context = {'form':form}
    return render(request,'admin/forms.html',context)

def view(request,pk):
    print(pk)
    bill = orders.objects.get(id = pk)
    # order = Order.objects.get(complete=False,invoice_id=bill)
    bill_total = bill.orderfinaltotal
    # order_item = []
    order_item = orderedcart.objects.filter(orderedid = bill)
    context = {'order_item' : order_item, 'bill' : bill , 'bill_total':bill_total}
    return render(request, 'order/index.html',context)

