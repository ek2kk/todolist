# Generated by Django 4.2.5 on 2023-09-05 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_todo_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 20, 18, 41, 33868), verbose_name='date and time created'),
        ),
    ]
