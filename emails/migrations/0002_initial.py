# Generated by Django 4.0.4 on 2022-08-10 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emails', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsendingfact',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
        migrations.AddField(
            model_name='emailsendingfact',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.emailtype'),
        ),
    ]