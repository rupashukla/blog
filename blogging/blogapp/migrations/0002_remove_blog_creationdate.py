# Generated by Django 4.2 on 2023-05-14 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='creationdate',
        ),
    ]
