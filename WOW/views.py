from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render
from WOW.forms import UserForm
from WOW.models import UserInfo

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', None)
            email = request.POST.get('email', None)
            User = UserInfo.objects.update_or_create(
                name = name,
                email = email,
                )
            message = 'Thanks for your signing'
            return render(request, 'index.html', {'message':message})
    else:
        form = UserForm()
        return render(request, 'index.html', {'form':form})
        
def items(request):
    items = Item.objects.all()
    return render(request, 'items.html', {'items':items})

def item_view(request, title):
    the_item = Item.objects.filter(title=title)
    return render(request, 'item.html', {'items':the_item})
    

