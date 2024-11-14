# Generated by Django 5.1.3 on 2024-11-14 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_code', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Customers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('code_item', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=9)),
                ('name_item', models.CharField(max_length=255)),
                ('maker', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'Items',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Storages',
            fields=[
                ('storages_id', models.AutoField(primary_key=True, serialize=False)),
                ('storage_address', models.CharField(max_length=255)),
                ('storage_manager', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Storages',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('sale_code', models.AutoField(primary_key=True, serialize=False)),
                ('sale_date', models.DateTimeField(blank=True, null=True)),
                ('sold_count', models.IntegerField()),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('code_item', models.ForeignKey(db_column='code_item', on_delete=django.db.models.deletion.CASCADE, to='myapp.items')),
                ('customer_code', models.ForeignKey(db_column='customer_code', on_delete=django.db.models.deletion.CASCADE, to='myapp.customers')),
            ],
            options={
                'db_table': 'Sales',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='items',
            name='storages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.storages'),
        ),
    ]