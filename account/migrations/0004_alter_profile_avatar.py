# Generated by Django 5.0.1 on 2024-09-14 19:57

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=account.models.avatar_upload_path),
        ),
    ]