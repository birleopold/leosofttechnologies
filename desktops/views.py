from django.shortcuts import render


# Create your views here.
from .models import Desktop


def desktop(request):
    products = Desktop.objects.all()
    context = { 'product':products }
    return render(request, 'desktops/list.html', context)