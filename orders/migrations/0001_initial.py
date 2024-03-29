# Generated by Django 4.0.4 on 2022-08-10 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='Адрес доставки')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Окончательная цена')),
                ('product_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Начальная цена')),
                ('comment', models.TextField(blank=True, default=None, null=True, verbose_name='Коментарий')),
                ('cupon', models.CharField(blank=True, default='', max_length=12, null=True, verbose_name='Купон')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='Тип статуса')),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статусы заказа',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(default=None, max_length=128, verbose_name='Сcылка на картинку')),
                ('nmb', models.IntegerField(default=1, verbose_name='Количество')),
                ('product_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена за штуку')),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена со скидкой')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена обшая')),
                ('review', models.TextField(blank=True, default=None, null=True, verbose_name='Отзыв')),
                ('is_active', models.BooleanField(default=True)),
                ('session_key', models.CharField(default=None, max_length=32, verbose_name='Ключ сессии')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'Продукт в заказе',
                'verbose_name_plural': 'Продукты в заказе',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.status'),
        ),
    ]
