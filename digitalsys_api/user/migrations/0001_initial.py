# Generated by Django 3.2.9 on 2023-06-22 22:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('profile', models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User')], default='USER', max_length=10)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]