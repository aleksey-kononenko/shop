# Generated by Django 4.0.4 on 2022-05-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=None, max_length=128, verbose_name='Адрес доставки'),
        ),
    ]
