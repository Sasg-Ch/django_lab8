# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    customer_code = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)

    class Meta:
        db_table = 'Customers'


class Items(models.Model):
    code_item = models.AutoField(primary_key=True)
    type = models.CharField(max_length=9)
    name_item = models.CharField(max_length=255)
    maker = models.CharField(max_length=255)
    storages = models.ForeignKey('Storages', models.DO_NOTHING)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Items'


class Sales(models.Model):
    sale_code = models.AutoField(primary_key=True)
    sale_date = models.DateTimeField(blank=True, null=True)
    customer_code = models.ForeignKey(Customers, models.DO_NOTHING, db_column='customer_code')
    code_item = models.ForeignKey(Items, models.DO_NOTHING, db_column='code_item')
    sold_count = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'Sales'


class Storages(models.Model):
    storages_id = models.AutoField(primary_key=True)
    storage_address = models.CharField(max_length=255)
    storage_manager = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        db_table = 'Storages'









