# Generated by Django 4.2.20 on 2025-05-23 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_backenduser_frontenduser_delete_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontenduser',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
