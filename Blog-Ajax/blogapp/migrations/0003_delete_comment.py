# Generated by Django 2.2.6 on 2019-10-09 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20191009_1820'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]