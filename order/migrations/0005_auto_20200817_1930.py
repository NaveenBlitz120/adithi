# Generated by Django 3.1 on 2020-08-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200817_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]