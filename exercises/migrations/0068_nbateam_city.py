# Generated by Django 3.1.5 on 2022-05-03 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0067_auto_20220503_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='nbateam',
            name='city',
            field=models.ForeignKey(default=295, on_delete=django.db.models.deletion.CASCADE, to='exercises.city'),
            preserve_default=False,
        ),
    ]