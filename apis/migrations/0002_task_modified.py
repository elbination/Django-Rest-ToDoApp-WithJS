# Generated by Django 3.0.8 on 2020-07-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
