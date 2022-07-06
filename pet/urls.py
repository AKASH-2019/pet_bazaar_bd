from django.urls import path
from pet import views

# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    # path('', views.hello_world, name='hello_world'),
    path('', views.home, name='home'),
    path('product/<slug>/<secondary_slug>', views.productPaginateByPetView, name='productPaginate'),
    path('product/<slug>', views.productSelect, name='productSelect'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('order/<id>', views.order, name='order'),
    path('order-list', views.orderList, name='orderList'),


    # request 
    path('product-paginate/pet', views.productPaginateByPet, name='productPaginateByPet'),
    path('orderUpsert', views.orderUpsert, name='orderUpsert'),

    path('ordeEmail', views.orderEmail, name='orderEmail'),
]
