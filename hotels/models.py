from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class City(models.Model):
    """ Модель города """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Hotel(models.Model):
    """ Модель отеля """
    name = models.CharField(verbose_name='Имя', max_length=200,
                            unique=True)
    address = models.CharField(verbose_name='Адрес', max_length=200)
    phone = PhoneNumberField(max_length=30, unique=True,
                             verbose_name='Телефон',
                             null=True, blank=True,)
    city = models.ForeignKey(City, verbose_name='Город',  on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    def __str__(self):
        return self.name
