# Generated by Django 3.0.5 on 2020-08-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_orderedcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('feedbackdata', models.TextField()),
            ],
        ),
    ]
