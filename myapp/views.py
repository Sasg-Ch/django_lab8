from django.shortcuts import render
from .models import Customers, Items, Sales, Storages


def index(request):
    storagess = Storages.objects.all()
    customers = Customers.objects.all()
    items = Items.objects.all()
    sales = Sales.objects.all()


    context = {
        'storagess': storagess,
        'customers': customers,
        'items': items,
        'sales': sales
    }

    return render(request, 'main/index.html', context)
