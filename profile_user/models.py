from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    """
    Информация о пользователе.
    """
    email = models.EmailField(verbose_name='Почта (mail)', unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    img_profile = models.ImageField(verbose_name='Фото', upload_to='profile_images/', blank=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class ProfileFollow(models.Model):
    """
    Система подписок одного пользователя на другого.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
    follow_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follows')
    created = models.DateTimeField(auto_now_add=True)
