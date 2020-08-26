from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import Create , Update , Update_order , Update_offer , Update_flower
from order.models import product , orders , orderedcart , setcart , flower, feedback
from .filters import myFilter , orderFilter , floFilter
from .decorators import allowed_user ,unauthenticated_user
from django.contrib.auth.decorators import login_required


st='/admin'
# Create your views here.
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def home(request):
    order = orders.objects.all()
    products = product.objects.all()
    feedbacks = feedback.objects.all()
    total_products = products.count()
    total_orders = order.count()
    completed = order.filter(status='completed').count()
    pending = order.filter(status='pending').count()
    orderfil = orderFilter(request.GET , queryset=order)
    order = orderfil.qs

    context = {'orders':order, 'products':products,
    'total_orders':total_orders,'completed':completed,
	'pending':pending ,'filter':orderfil , 'feedbacks':feedbacks }
    return render(request, 'admin/dashboard.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def stock(request):
    prod_obj = product.objects.all()
    myfilter = myFilter(request.GET,queryset=prod_obj)
    prod_obj= myfilter.qs
    context ={ 'prod':prod_obj , 'filter':myfilter  }
    print(prod_obj ,context['prod'])
    return render(request, 'admin/search.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def stockflo(request):
    flow_obj = flower.objects.all()
    myfilter = floFilter(request.GET,queryset=flow_obj)
    flow_obj= myfilter.qs
    context ={ 'prod':flow_obj , 'filter':myfilter ,'type':'flower' }
    print(flow_obj ,context['prod'])
    return render(request, 'admin/search.html',context)

@login_required(login_url='login')
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


@login_required(login_url='login')
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

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateflo(request,pk):

    order = flower.objects.get(id=pk)
    form = Update_flower(instance=order)
    if request.method == 'POST':
        form = Update_flower(request.POST,instance = order)
        if form.is_valid():
            form.save()
            return redirect(st)


    context = {'form':form}
    return render(request,'admin/forms.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def delete(request,pk):

    order = product.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect(st)

    context = {'item':order}
    return render(request,'admin/delete.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteflo(request,pk):

    order = flower.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect(st)

    context = {'item':order}
    return render(request,'admin/delete.html',context)


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

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
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

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def view(request,pk):
    print(pk)
    bill = orders.objects.get(id = pk)
    # order = Order.objects.get(complete=False,invoice_id=bill)
    bill_total = bill.orderfinaltotal
    # order_item = []
    order_item = orderedcart.objects.filter(orderedid = bill)
    context = {'order_item' : order_item, 'bill' : bill , 'bill_total':bill_total}
    return render(request, 'admin/index.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def update_offer(request):

    setcarts = setcart.objects.get(id=1)
    form = Update_offer(instance=setcarts)
    if request.method == 'POST':
        form = Update_offer(request.POST,instance = setcarts)
        if form.is_valid():
            form.save()
            return redirect(st)


    context = {'form':form}
    return render(request,'admin/forms.html',context)
