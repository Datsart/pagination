from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def product_list(request):
    products = Product.objects.order_by('id')
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'products': page_obj})
