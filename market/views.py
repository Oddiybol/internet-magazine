from itertools import product
from unicodedata import category
from django.shortcuts import render
from market.models import Category, Product
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    categories = Category.objects.all()
    count_cat = categories.count()
    print(count_cat)
    return render(request, 'index.html',{'categories':categories, 'count_categories':count_cat})

    # return render(request, '')

    return HttpResponse('Hello world!')

def base(request):
    return render(request, 'base.html')
    # return HttpResponse('<h1><i>BASE HTML!</i></h1>')

def suit(request):
    product = Product.objects.all()
    title='Костюм'
    return render(request, 'suit.html', {'title':title,'products':product})

def cart(request):
    title = 'cart'
    return render(request, 'cart.html',{'title':title})
