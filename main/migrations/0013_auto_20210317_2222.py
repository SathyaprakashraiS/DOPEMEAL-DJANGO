# Generated by Django 3.1.3 on 2021-03-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_shopper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopper',
            name='productname',
            field=models.CharField(max_length=1000),
        ),
    ]
