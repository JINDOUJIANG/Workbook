# Generated by Django 3.1.5 on 2021-12-03 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0042_auto_20211203_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit_card',
            name='identification',
        ),
    ]