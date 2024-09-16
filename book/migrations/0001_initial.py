# Generated by Django 5.0.1 on 2024-09-16 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('author', models.CharField(max_length=50)),
                ('translator', models.CharField(blank=True, max_length=50, null=True)),
                ('publisher', models.CharField(blank=True, max_length=50, null=True)),
                ('ISBN', models.CharField(blank=True, max_length=25, null=True)),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('book_size', models.CharField(blank=True, max_length=50, null=True)),
                ('cover_type', models.CharField(blank=True, max_length=50, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('number_of_pages', models.IntegerField()),
            ],
            bases=('product.product',),
        ),
    ]
