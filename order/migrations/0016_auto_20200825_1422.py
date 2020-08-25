# Generated by Django 3.0.5 on 2020-08-25 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20200825_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedcart',
            name='pfid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.flower'),
        ),
        migrations.AlterField(
            model_name='orderedcart',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.product'),
        ),
    ]
