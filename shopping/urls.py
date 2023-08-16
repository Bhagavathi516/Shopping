from django.urls import path
from .views import item_list, item_create, item_detail, item_update,item_delete

urlpatterns = [
    path('', item_list, name ='item_list'),
    path('item/create/', item_create, name='item_create'),
    path('item/<id>/', item_detail, name='item_detail'),
    path('item/<id>/update', item_update, name='item_update'),
    path('item/<id>/delete', item_delete, name='item_delete')
]
