# Generated by Django 3.2.3 on 2021-12-01 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='user',
            new_name='user_id',
        ),
    ]
