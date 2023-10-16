from django.db import models, connection

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    picture = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    change_date = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.product_name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    created_at = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')