from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import Create , Update , Update_order , Update_offer , Update_flower , CreateFlo , Update_service , CreateSer
from order.models import product , orders , orderedcart , setcart , flower, feedback , service
from .filters import myFilter , orderFilter , floFilter , serFilter
from .decorators import allowed_user ,unauthenticated_user
from django.contrib.auth.decorators import login_required


st='/admin'
# Create your views here.
@login_required(login_url='login')
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
	'pending':pending ,'filter':orderfil  }
    return render(request, 'admin/dashboard.html', context)

def feedbackpage(request):
    feedbacks = feedback.objects.all()
    context ={
        'feedbacks':feedbacks
    }
    return render(request, 'admin/feedback.html', context)

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
def stockservice(request):
    serv_obj = service.objects.all()
    myfilter = serFilter(request.GET,queryset=serv_obj)
    serv_obj= myfilter.qs
    context ={ 'prod':serv_obj , 'filter':myfilter }
    print(serv_obj ,context['prod'])
    return render(request, 'admin/dashboard1.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def create(request):

    form = Create(initial={'groceries_category': 'Null' })
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
def createflo(request):

    form = CreateFlo()
    context = {'form':form,}
    if request.method == 'POST':
        #print('printing POST:',request.POST)
        form = CreateFlo(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect(st)

    return render(request,'admin/forms.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def createser(request):

    form = CreateSer()
    context = {'form':form,}
    if request.method == 'POST':
        #print('printing POST:',request.POST)
        form = CreateSer(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect(st)

    return render(request,'admin/forms.html',context)



@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def update(request,pk):

    order = product.objects.get(id=pk)
    form = Update(instance=order)
    form.fields['our_price'].widget.attrs = {'class' : 'form-control' }
    form.fields['market_price' ].widget.attrs = {'class' : 'form-control' }
    form.fields['types'].widget.attrs = {'class' : 'form-control' }
    form.fields['name'].widget.attrs = {'class' : 'form-control' }
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
    form.fields['our_price'].widget.attrs = {'class' : 'form-control' }
    form.fields['market_price' ].widget.attrs = {'class' : 'form-control' }
    form.fields['name'].widget.attrs = {'class' : 'form-control' }
    if request.method == 'POST':
        form = Update_flower(request.POST,instance = order)
        if form.is_valid():
            form.save()
            return redirect(st)


    context = {'form':form}
    return render(request,'admin/forms.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateser(request,pk):

    order = service.objects.get(id=pk)
    form = Update_service(instance=order)
    form.fields['area'].widget.attrs = {'class' : 'form-control' }
    form.fields['rate' ].widget.attrs = {'class' : 'form-control' }
    if request.method == 'POST':
        form = Update_service(request.POST,instance = order)
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

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteser(request,pk):

    order = service.objects.get(id=pk)
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
    form.fields['status'].widget.attrs = {'class' : 'form-control' }
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
    return render(request, 'admin/invoice.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def update_offer(request):

    setcarts = setcart.objects.get(id=1)
    form = Update_offer(instance=setcarts)
    form.fields['minimum_cart_value'].widget.attrs = {'class' : 'form-control' }
    form.fields['offer_on_or_off'].widget.attrs = {'class' : 'form-control' }
    form.fields['silveroff_value'].widget.attrs = {'class' : 'form-control' }
    form.fields['silveroff_percentage'].widget.attrs = {'class' : 'form-control' }
    form.fields['goldenoff_percentage'].widget.attrs = {'class' : 'form-control' }
    form.fields['goldenoff_value'].widget.attrs = {'class' : 'form-control' }
    form.fields['platinumoff_value'].widget.attrs = {'class' : 'form-control' }
    form.fields['platinumoff_percentage'].widget.attrs = {'class' : 'form-control' }
    form.fields['phoneno'].widget.attrs = {'class' : 'form-control' }

    if request.method == 'POST':
        form = Update_offer(request.POST,instance = setcarts)
        if form.is_valid():
            form.save()
            return redirect(st)


    context = {'form':form}
    return render(request,'admin/forms.html',context)

def geo(request):
    return render(request,'admin/geo.html')