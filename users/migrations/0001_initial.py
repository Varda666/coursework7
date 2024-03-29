# Generated by Django 4.2.8 on 2024-01-11 18:11

from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_role', models.CharField(choices=[('member', 'member'), ('moderator', 'moderator'), ('owner', 'owner')], default='member', verbose_name='роль')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('last_login', models.DateField(default=django.utils.timezone.now, verbose_name='дата последнего посещения')),
                ('is_staff', models.BooleanField(default=False, verbose_name='статус staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='статус активности')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', users.models.MyUserManager()),
            ],
        ),
    ]
