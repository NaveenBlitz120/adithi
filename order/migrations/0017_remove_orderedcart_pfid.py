# Generated by Django 3.0.5 on 2020-08-25 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20200825_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedcart',
            name='pfid',
        ),
    ]
