# Generated by Django 4.0.4 on 2022-06-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cupon',
            field=models.CharField(blank=True, default='', max_length=12, null=True, verbose_name='Купон'),
        ),
        migrations.AddField(
            model_name='order',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Начальная цена'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='img',
            field=models.CharField(default=None, max_length=128, verbose_name='Сcылка на картинку'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена за штуку'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='review',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Окончательная цена'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена со скидкой'),
        ),
    ]