# Generated by Django 3.1.5 on 2021-11-23 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0038_remove_message_is_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]
