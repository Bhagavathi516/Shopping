from django.shortcuts import render, redirect, get_object_or_404
from .models import shoppingItemModel
from .forms import shoppingItemForm
from users.decorators import superuser_required
from django.urls import reverse
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import permissions
from shopping.serializers import shoppingItemSerializer

# Create your views here. 
@superuser_required
def item_create(request):
    if request.user.is_superuser:
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

@superuser_required
def item_update(request, id):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(shoppingItemModel, item_id = id)
        form = shoppingItemForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('item_detail', obj.item_id)
        context['form']=form
    return render(request, "shopping/item_update.html", context)

@superuser_required 
def item_delete(request, id):
    if request.user.is_superuser:
        context = {}
        item = get_object_or_404(shoppingItemModel, item_id = id)
        if request.method == "POST":
            item.delete()
            return redirect('item_list')
        context['item'] = item
    return render(request, "shopping/item_delete.html", context)


class shoppingItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = shoppingItemModel.objects.all()
    serializer_class = shoppingItemSerializer
    permission_classes = [permissions.IsAuthenticated]