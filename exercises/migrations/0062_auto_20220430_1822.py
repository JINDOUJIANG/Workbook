# Generated by Django 3.1.5 on 2022-04-30 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0061_auto_20220430_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nbateam',
            name='city',
            field=models.CharField(default='las vegas', max_length=255),
        ),
        migrations.AlterField(
            model_name='nbateam',
            name='worth',
            field=models.IntegerField(default=800),
        ),
    ]
