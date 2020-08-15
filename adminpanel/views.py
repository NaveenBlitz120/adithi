from django.shortcuts import render ,redirect
from .forms import Create

# Create your views here.
def create(request):
    
    form = Create()

    context = {'form':form,}
    if request.method == 'POST':
        #print('printing POST:',request.POST)
        form = Create(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('/stock')

    return render(request,'admin/forms.html',context)