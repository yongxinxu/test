from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def items(request):
    items = Item.objects.all()
    return render(request, 'items.html', {'items':items})

def item_view(request, title):
    the_item = Item.objects.filter(title=title)
    return render(request, 'item.html', {'items':the_item})
    

# forms
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
