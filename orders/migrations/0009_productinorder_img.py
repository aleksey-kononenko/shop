# Generated by Django 4.0.4 on 2022-06-22 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_productinorder_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='img',
            field=models.CharField(default=None, max_length=128, verbose_name='Сcылка на картинку'),
        ),
    ]
