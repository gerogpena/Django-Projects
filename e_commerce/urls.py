from django.urls import path
from .import views

app_name = 'e_commerce'

urlpatterns = [
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('product-list/', views.product_list, name='product_list'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-category/', views.add_category, name='add_category'),
    path('confirm-order/', views.confirm_order, name='confirm_order'),
]
