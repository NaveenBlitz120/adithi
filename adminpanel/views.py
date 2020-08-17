from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import Create , Update
from order.models import product
from .filters import myFilter

st='/stock'
# Create your views here.
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

def success(request):
    return HttpResponse('your task completed successfully')

def stock(request):
    prod_obj = product.objects.all()
    myfilter = myFilter(request.GET,queryset=prod_obj)
    prod_obj= myfilter.qs
    
    context ={ 'prod':prod_obj , 'filter':myfilter  }
    print(prod_obj ,context['prod'])
    
    return render(request, 'admin/search.html',context)

def delete(request,pk):
    
    order = product.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect(st)

    context = {'item':order}
    return render(request,'admin/delete.html',context)

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

