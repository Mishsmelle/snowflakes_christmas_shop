# Generated by Django 3.2.8 on 2021-11-30 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]