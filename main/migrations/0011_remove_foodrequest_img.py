# Generated by Django 3.1.3 on 2021-03-17 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210317_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodrequest',
            name='img',
        ),
    ]
