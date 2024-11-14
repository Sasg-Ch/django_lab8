from django.contrib import admin
from .models import Customers, Items, Sales, Storages
admin.site.register(Customers)
admin.site.register(Items)
admin.site.register(Sales)
admin.site.register(Storages)