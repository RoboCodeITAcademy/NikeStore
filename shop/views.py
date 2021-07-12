from django.shortcuts import render, get_object_or_404
from django.views.generic import (
	ListView,
	DetailView,)
from .models import *

# Create your views here.

class HomePageView(ListView):
	model = Product
	paginate_by = 3
	template_name = 'index.html'

class ProductDetailView(DetailView):
	model = Product

def categoryDetail(request,category_slug):
	category = get_object_or_404(Category,slug=category_slug)
	products = Product.objects.filter(category=category)
	context = {
		'products':products
	}
	return render(request, 'product_list.html', context)


def tagDetail(request,tag_slug):
	tag = get_object_or_404(Tag,slug=tag_slug)
	products = Product.objects.filter(tag=tag)
	context = {
		'products':products
	}
	return render(request, 'product_list.html', context)