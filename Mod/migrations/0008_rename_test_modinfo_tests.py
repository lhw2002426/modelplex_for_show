# Generated by Django 3.2.12 on 2022-04-23 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mod', '0007_modinfo_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modinfo',
            old_name='test',
            new_name='tests',
        ),
    ]