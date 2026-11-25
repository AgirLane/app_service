from django.db import models

class Category(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('Тег', max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    objects = models.Manager()
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст', blank=True)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    is_published = models.BooleanField('Опубликован', default=True)
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,
                                verbose_name='Категория',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name='posts',)
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True, related_name='posts')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'




    def __str__(self):
        return self.title





