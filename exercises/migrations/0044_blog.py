# Generated by Django 3.1.5 on 2021-12-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0043_remove_credit_card_identification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=100)),
            ],
        ),
    ]