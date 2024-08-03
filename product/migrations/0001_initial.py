# Generated by Django 5.0.1 on 2024-08-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=120)),
                ('price', models.FloatField()),
                ('discount', models.FloatField(blank=True, default=0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
