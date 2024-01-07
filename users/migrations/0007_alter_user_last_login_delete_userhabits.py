# Generated by Django 4.2.8 on 2024-01-07 00:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='дата последнего посещения'),
        ),
        migrations.DeleteModel(
            name='UserHabits',
        ),
    ]
