from django.shortcuts import render
from gogreenapp.models import Item



def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def products(request):
    item = Item.objects.all()
    context = {'item':item}
    return render(request,'products.html',context)


def contact(request):
    return render(request,'contact.html')
