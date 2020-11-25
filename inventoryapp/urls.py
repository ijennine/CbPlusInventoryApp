from django.urls import path

from . import views

app_name = 'inventoryapp'
urlpatterns = [
    # ex: /InventoryApp/
    path('', views.list, name='list'),
    # ex: 
    path('modify/<int:product_ref>/', views.modify, name='modify'),
    # ex: 
    path('productForm/', views.addProductForm, name='productForm')
]