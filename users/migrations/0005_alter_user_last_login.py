# Generated by Django 4.2.8 on 2023-12-21 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_managers_alter_user_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2023, 12, 22, 0, 48, 33, 915919), verbose_name='дата последнего посещения'),
        ),
    ]