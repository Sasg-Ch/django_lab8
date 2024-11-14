from django.db import models

# Модель для клієнтів
class Customers(models.Model):
    customer_code = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)

    class Meta:
        managed = True  # Це дозволить Django керувати таблицею (без managed=False)
        db_table = 'Customers'

    def __str__(self):
        return self.customer_name


# Модель для складів
class Storages(models.Model):
    storages_id = models.AutoField(primary_key=True)
    storage_address = models.CharField(max_length=255)
    storage_manager = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'Storages'

    def __str__(self):
        return self.storage_address


# Модель для товарів
class Items(models.Model):
    code_item = models.AutoField(primary_key=True)
    type = models.CharField(max_length=9)
    name_item = models.CharField(max_length=255)
    maker = models.CharField(max_length=255)
    storages = models.ForeignKey(Storages, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'Items'

    def __str__(self):
        return self.name_item


# Модель для продажів
class Sales(models.Model):
    sale_code = models.AutoField(primary_key=True)
    sale_date = models.DateTimeField(blank=True, null=True)
    customer_code = models.ForeignKey(Customers, on_delete=models.CASCADE, db_column='customer_code')
    code_item = models.ForeignKey(Items, on_delete=models.CASCADE, db_column='code_item')
    sold_count = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Sales'

    def __str__(self):
        return f"Sale {self.sale_code} for {self.customer_code.customer_name} on {self.sale_date}"