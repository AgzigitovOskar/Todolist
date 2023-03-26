from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # при регистрации запрос по login and password
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
