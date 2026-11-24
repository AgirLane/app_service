from django.db import models


class Post(models.Model):

    objects = models.Manager()
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст', blank=True)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    is_published = models.BooleanField('Опубликован', default=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
