# Generated by Django 4.2.1 on 2023-10-28 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='GTIN',
            new_name='gtin',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='NCM',
            new_name='ncm',
        ),
    ]
