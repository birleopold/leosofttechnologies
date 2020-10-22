from django.shortcuts import render


# Create your views here.
from .models import Project


def projects(request):
    products = Project.objects.all()
    context = { 'product':products }
    return render(request, 'developer/list.html', context)