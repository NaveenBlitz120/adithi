# Generated by Django 3.0.5 on 2020-08-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_orderedcart_quantity_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='grade',
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('orderconfirmed', 'orderconfirmed'), ('cancelled', 'cancelled'), ('completed', 'completed')], default='pending', max_length=20),
        ),
    ]