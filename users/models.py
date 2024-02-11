from django.db import models
from django.contrib.auth.models import AbstractUser


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Модель для пользователя
    """
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
