from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Информация о пользователе + его подписки, подписчики.
    """
    first_name = models.CharField('имя', max_length=50, blank=True)
    last_name = models.CharField('фамилия', max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscriptions = models.TextField('подписки', blank=True)
    my_subscribers = models.TextField('мои подписчики', blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)
