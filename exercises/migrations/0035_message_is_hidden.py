# Generated by Django 3.1.5 on 2021-11-19 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0034_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]