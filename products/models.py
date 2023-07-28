from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя товара')
    weight = models.FloatField(verbose_name='Вес товара')
    color = models.CharField(max_length=30, verbose_name='Цвет товара')
    amount = models.IntegerField(verbose_name='Количество')
    discription = models.TextField(verbose_name='Описание товара')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.name
