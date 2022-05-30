from django.db import models


class Color(models.Model):
    color = models.CharField('Цвет', max_length=64)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Type(models.Model):
    type = models.CharField('Вид', max_length=64)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Category(models.Model):
    category = models.CharField('Категория', max_length=64)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Textile(models.Model):
    textile = models.CharField('Вид ткани', max_length=64)

    def __str__(self):
        return self.textile

    class Meta:
        verbose_name = 'Вид ткани'
        verbose_name_plural = 'Виды ткани'


class Country(models.Model):
    country = models.CharField('Страна-производитель', max_length=64)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Product(models.Model):
    name = models.CharField('Наименование', max_length=128)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    textile = models.ForeignKey(Textile, blank=True, null=True, default=None, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, blank=True, null=True, default=None, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, blank=True, null=True, default=None, on_delete=models.CASCADE)
    thread = models.CharField('Вид ниток', max_length=64, blank=True, null=True, default=None)
    material = models.CharField('Материал', max_length=64, blank=True, null=True, default=None)
    length = models.DecimalField('Длина мотка', max_digits=4, decimal_places=1, blank=True, null=True, default=None)
    themes = models.CharField('Тематика', max_length=64, blank=True, null=True, default=None)
    technique = models.CharField('Техника', max_length=64, blank=True, null=True, default=None)
    stitching = models.CharField('Зашивка', max_length=64, blank=True, null=True, default=None)
    dimension = models.CharField('Размер', max_length=128, blank=True, null=True, default=None)
    purpose = models.CharField('Назначение', max_length=256, blank=True, null=True, default=None)
    equipment = models.CharField('Комплектация', max_length=256, blank=True, null=True, default=None)
    num_color = models.IntegerField('Количество цветов', blank=True, null=True, default=None)
    num_bead = models.IntegerField('Количество бусин', blank=True, null=True, default=None)
    description = models.TextField('Описание', blank=True, null=True, default=None)
    discount = models.IntegerField('Скидка', default=0)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2, blank=True, null=True, default=0.0)
    is_active = models.BooleanField('Актуальность', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='products_images')
    is_main = models.BooleanField('Главная', default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'