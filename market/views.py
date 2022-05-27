from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')
    # return render(request, '')

    return HttpResponse('Hello world!')

def base(request):
    return render(request, 'base.html')
    # return HttpResponse('<h1><i>BASE HTML!</i></h1>')

def suit(request):
    title='Костюм'
    return render(request, 'suit.html', {'title':title})

