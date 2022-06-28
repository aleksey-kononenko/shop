from django.db import models


class Slider(models.Model):
    name = models.CharField('Наименование', max_length=128, default=None)
    slider = models.ImageField(upload_to='slider', default='default.jpg')
    is_show = models.BooleanField('Видимость', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'
