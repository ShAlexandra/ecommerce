from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=256)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Наименование', max_length=256)
    price = models.DecimalField('Стоимость', max_digits=6, decimal_places=2)
    year = models.IntegerField('Год создания', default=2020, blank=True, null=True)
    content = models.TextField('Описание')
    categories = models.ForeignKey(Category, verbose_name='Категории', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Image(models.Model):
    alt = models.CharField('Название', max_length=256)
    image = models.ImageField('Изображение', upload_to='images/')
    product = models.ForeignKey(Product, verbose_name='Изображение товара', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self):
        return self.alt