# Generated by Django 2.2.4 on 2019-08-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190822_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]