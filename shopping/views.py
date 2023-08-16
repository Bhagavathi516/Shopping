from django.shortcuts import render, redirect, get_object_or_404
from .models import shoppingItemModel
from .forms import shoppingItemForm
from django.http import HttpResponse

# Create your views here. 
def item_create(request):
    context = {}
    form = shoppingItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return HttpResponse('Item is successfully created')
        return redirect('item_list')
    context['form'] = form
    return render(request, "shopping/item_create.html", context)

def item_list(request):
    context = {}
    context["items"] = shoppingItemModel.objects.all()
    return render(request, "shopping/item_list.html", context)

def item_detail(request, id):
    context = {}
    context['item'] = shoppingItemModel.objects.get(item_id = id)
    return render(request, "shopping/item_detail.html", context)

def item_update(request, id):
    context = {}
    obj = get_object_or_404(shoppingItemModel, item_id = id)
    form = shoppingItemForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('item_detail', obj.item_id)
    context['form']=form
    return render(request, "shopping/item_update.html", context)
    
def item_delete(request, id):
    context = {}
    item = get_object_or_404(shoppingItemModel, item_id = id)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    context['item'] = item
    return render(request, "shopping/item_delete.html", context)
