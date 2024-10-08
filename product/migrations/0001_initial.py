# Generated by Django 5.0.1 on 2024-10-04 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhysicalBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount', models.FloatField(blank=True, default=0, null=True)),
                ('stock', models.PositiveIntegerField(default=0, help_text='Number of items in stock')),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('author', models.CharField(help_text='Author of the book', max_length=100)),
                ('translator', models.CharField(blank=True, max_length=100, null=True)),
                ('publication_name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(help_text='URL-friendly identifier for the book', max_length=200, unique=True)),
                ('cover_image', models.ImageField(help_text='Cover image of the book', upload_to='book_covers/')),
                ('ISBN', models.CharField(blank=True, max_length=25, null=True)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('weight', models.DecimalField(decimal_places=2, help_text='Weight of the book in kilograms', max_digits=5)),
                ('dimensions', models.CharField(help_text='Dimensions of the book (e.g., 8x11x2 inches)', max_length=100)),
                ('cover_type', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_pages', models.IntegerField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount', models.FloatField(blank=True, default=0, null=True)),
                ('stock', models.PositiveIntegerField(default=0, help_text='Number of items in stock')),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('author', models.CharField(help_text='Author of the book', max_length=100)),
                ('translator', models.CharField(blank=True, max_length=100, null=True)),
                ('publication_name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(help_text='URL-friendly identifier for the book', max_length=200, unique=True)),
                ('cover_image', models.ImageField(help_text='Cover image of the book', upload_to='book_covers/')),
                ('ISBN', models.CharField(blank=True, max_length=25, null=True)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('file_format', models.CharField(choices=[('pdf', 'PDF'), ('epub', 'EPUB'), ('mobi', 'MOBI')], max_length=50)),
                ('download_url', models.URLField(help_text='URL to download the e-book')),
                ('file_size', models.DecimalField(decimal_places=2, help_text='File size in MB', max_digits=6)),
                ('number_of_pages', models.PositiveIntegerField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AudioBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount', models.FloatField(blank=True, default=0, null=True)),
                ('stock', models.PositiveIntegerField(default=0, help_text='Number of items in stock')),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('author', models.CharField(help_text='Author of the book', max_length=100)),
                ('translator', models.CharField(blank=True, max_length=100, null=True)),
                ('publication_name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(help_text='URL-friendly identifier for the book', max_length=200, unique=True)),
                ('cover_image', models.ImageField(help_text='Cover image of the book', upload_to='book_covers/')),
                ('ISBN', models.CharField(blank=True, max_length=25, null=True)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('audio_length', models.DurationField(help_text='Total length of the audio book')),
                ('narrator', models.CharField(max_length=100)),
                ('audio_url', models.URLField(help_text='URL to listen to the audio book')),
                ('episode_count', models.PositiveIntegerField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producttype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
