# Generated by Django 3.1.5 on 2021-12-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0040_credit_card_identification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit_card',
            name='identification',
            field=models.IntegerField(),
        ),
    ]