from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Item,Menu



def details(request,pk):

    item = Item.objects.filter(fkmenu_id=pk)
    children = Item

    template_name = 'menu/menu.html'
    context = {
    'items': item,
    'children':children
    }
    return render(request,template_name,context)
