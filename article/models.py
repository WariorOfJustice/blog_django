from django.db import models

from profile_user.models import Profile


class Article(models.Model):
    """
    Информация о статье.
    """
    title = models.CharField('Название поста', max_length=255, db_index=True)
    text = models.TextField('Текст поста', db_index=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField('Время создания поста', auto_now_add=True)
    updated = models.DateTimeField('Время обновления поста', auto_now=True)
    rubric = models.CharField('Тема поста', max_length=150, blank=True, db_index=True)
    objects = models.Manager()

    def get_start_text(self):
        """
        Возвращает краткое содержание текста статьи.
        """
        if len(self.text) > 140:
            index_last_word = self.text[:150].rfind(' ')
            start_text = self.text[:index_last_word] + '...'
        else:
            start_text = self.text
        return start_text

    class Meta:
        ordering = ['-created']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Информация о комментарии.
    """
    text = models.TextField('Текст комментария')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField('Время создания комментария', auto_now_add=True)
    updated = models.DateTimeField('Время обновления комментария', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-updated', '-created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:20] + '...'
