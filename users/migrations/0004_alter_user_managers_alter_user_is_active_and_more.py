# Generated by Django 4.2.8 on 2023-12-21 21:33

import datetime
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_is_active_alter_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.MyUserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='статус активности'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='статус staff'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2023, 12, 22, 0, 33, 15, 493912), verbose_name='дата последнего посещения'),
        ),
    ]
