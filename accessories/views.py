from django.shortcuts import render


# Create your views here.
from .models import Accessory


def accessories(request):
    products = Accessory.objects.all()
    context = { 'product':products }
    return render(request, 'accessories/list.html', context)







