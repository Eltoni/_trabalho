# Generated by Django 2.0 on 2018-01-17 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_entry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
    ]