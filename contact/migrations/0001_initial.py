# Generated by Django 3.2.8 on 2021-11-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(choices=[('general', 'General Questions'), ('product_information', 'Product Information'), ('order_status', 'Order Status'), ('shipping_delivery', 'Shipping and Delivery'), ('bulk_purchasing', 'Wholesale Purchasing')], default='general', max_length=254)),
                ('message', models.TextField()),
                ('message_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'ordering': ('-message_date',),
            },
        ),
    ]