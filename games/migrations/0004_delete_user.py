# Generated by Django 4.2.6 on 2024-06-09 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
