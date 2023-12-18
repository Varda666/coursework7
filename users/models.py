from datetime import datetime, date

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class MyUserManager(UserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        user = User.objects.create(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user





class User(AbstractUser):
    member = 'member'
    USER_ROLE_CHOISES = [
        ('member', 'member'),
        ('moderator', 'moderator'),
        ('owner', 'owner')
    ]

    username = None
    first_name = None
    last_name = None
    user_role = models.CharField(choices=USER_ROLE_CHOISES, default=member, verbose_name='роль')
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=150, verbose_name='имя')
    last_login = models.DateField(default=datetime.now(), verbose_name='дата последнего посещения')
    is_staff = models.BooleanField(default=False, verbose_name="статус staff")
    is_active = models.BooleanField(default=True, verbose_name="статус активности")

    objects = MyUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserHabits(models.Model):
    status = models.BooleanField(default=False, verbose_name="статус выполнения")
    date = models.DateField(verbose_name='дата выполнения привычки')
    user = models.ForeignKey(to='User', to_field='email', verbose_name='пользователь', on_delete=models.DO_NOTHING)
    habit = models.ForeignKey(to='useful_habits.Habit', to_field='id', verbose_name='привычка', on_delete=models.DO_NOTHING)