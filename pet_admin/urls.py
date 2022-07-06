from django.urls import path
from pet_admin import views
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    
    path('order-list', views.orderList, name='adminOrderList'),


    # request 
    path('order/status/update', views.orderStatusUpsert, name='orderStatusUpsert')
]
