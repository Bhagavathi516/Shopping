from django.urls import include, path
from .views import item_list, item_create, item_detail, item_update,item_delete

from rest_framework import routers
from shopping import views

router = routers.DefaultRouter()
router.register(r'shopping', views.shoppingItemViewSet)

urlpatterns = [
    path('', item_list, name ='item_list'),
    path('item/create/', item_create, name='item_create'),
    path('item/<id>/', item_detail, name='item_detail'),
    path('item/<id>/update', item_update, name='item_update'),
    path('item/<id>/delete', item_delete, name='item_delete'),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
