from django.shortcuts import render
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

