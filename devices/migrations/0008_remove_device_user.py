# Generated by Django 5.0.7 on 2024-12-29 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0007_alter_device_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='user',
        ),
    ]
