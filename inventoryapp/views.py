from datetime import date

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Product
from .forms import ProductForm, ModifyForm

def list(request):
    db_products_list = Product.objects.all().order_by('expiry_date')
    products_list = []
    expired_products = []
    
    for product in db_products_list:
        if product not in products_list:
            products_list.append(product)
        elif product in products_list and product.expiry_date < products_list[products_list.index(product)].expiry_date:
            products_list[products_list.index(product)] = product

    for product in products_list:
        if product.expiry_date <= date.today():
            expired_products.append(product)

    context = {'products_list' : products_list, 'expired_products': expired_products}
    return render(request, 'inventoryapp/list.html', context)

def modify(request, product_ref):
    product = get_object_or_404(Product, pk=product_ref)

    if request.method == 'POST':

        form = ModifyForm(request.POST)

        if form.is_valid():
            
            product.expiry_date = form.cleaned_data['product_expiry_date']
            product.save()

            return HttpResponseRedirect(reverse('inventoryapp:list'))
        
    else:
        form = ModifyForm()

    context = {
        'form': form,
        'product': product,
    }
    
    return render(request, 'inventoryapp/modify.html', context)

def addProductForm(request):
    gtin_list = [o.product_gtin for o in Product.objects.all()]

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        form = ProductForm(request.POST)

        if form.is_valid():

            product = Product(product_gtin=form.cleaned_data['product_gtin'], expiry_date=form.cleaned_data['product_expiry_date'])
            productFromDb = Product.objects.filter(pk=product.product_gtin)
            
            if (product.product_gtin in gtin_list) and productFromDb.values('expiry_date') > product.expiry_date:
                Product.objects.filter(pk=product.product_gtin).update(expiry_date=form.cleaned_data['product_expiry_date'])

            else:
                product.save()
            return HttpResponseRedirect(reverse('inventoryapp:list'))

    else:
        form = ProductForm()

    return render(request, 'inventoryapp/productForm.html', {'form': form})
