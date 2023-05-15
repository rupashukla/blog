# Generated by Django 4.2 on 2023-05-14 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogid', models.TextField(default='', max_length=100)),
                ('blogtitle', models.TextField(blank=True, null=True)),
                ('description', models.TextField(max_length=100)),
                ('Content', models.TextField(max_length=100)),
                ('creationdate', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.TextField(max_length=100)),
                ('name', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeid', models.TextField(max_length=100)),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.user')),
                ('blogid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.blog')),
            ],
        ),
    ]
