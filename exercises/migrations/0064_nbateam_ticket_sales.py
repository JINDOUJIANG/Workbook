# Generated by Django 3.1.5 on 2022-04-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0063_auto_20220430_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='nbateam',
            name='ticket_sales',
            field=models.IntegerField(default=3000),
            preserve_default=False,
        ),
    ]
