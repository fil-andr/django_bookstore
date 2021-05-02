from django.db import models


class Books(models.Model):
    book_title = models.CharField(max_length=50, verbose_name='Название книги')
    short_desc = models.TextField(blank=True, null=True, verbose_name='Краткое содержание')
    book_price = models.FloatField(blank=True, null=True, verbose_name='Цена')
    authors = models.ForeignKey('Authors', null=True, on_delete=models.PROTECT, verbose_name='Автор')

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
        ordering = ['book_title']


class Authors(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Автор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'