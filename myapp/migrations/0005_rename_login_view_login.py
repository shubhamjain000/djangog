# Generated by Django 5.1.2 on 2024-10-11 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_login_view_delete_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login_view',
            new_name='Login',
        ),
    ]
