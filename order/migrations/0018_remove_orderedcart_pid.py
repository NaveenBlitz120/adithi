# Generated by Django 3.0.5 on 2020-08-25 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_remove_orderedcart_pfid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedcart',
            name='pid',
        ),
    ]
