from django.utils.timezone import now
from django.db import models


DOLLAR = "Доллар"
SOUM = "Сум"
EURO = "Евро"
CURRENCY = [
    (DOLLAR, (DOLLAR)),
    (SOUM, (SOUM)),
    (EURO, (EURO)),
]


LAND = "Участок"
FLAT = "Квартира"
ESTATE_TYPE = [
    (LAND, ('Участок недвижимости')),
    (FLAT, ('Квартира')),
]
class User(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    birthday = models.DateField(verbose_name="День рождения")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name="Категории", max_length=64)

    def __str__(self):
        return self.name


class Estate(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255, null=True, blank=True) 
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    author = models.ForeignKey(User,  on_delete=models.CASCADE,  null=True, blank=True)
    price = models.PositiveBigIntegerField(verbose_name="Цена")
    currency = models.CharField(verbose_name="Валюта", max_length=32, choices=CURRENCY, default=DOLLAR)
    area = models.PositiveIntegerField(verbose_name="Площадь")
    room_amount = models.PositiveSmallIntegerField(verbose_name="Количество комнат")
    type = models.CharField(verbose_name="Тип недвижимости", max_length=64, choices=ESTATE_TYPE, default=FLAT)
    categories = models.ManyToManyField(Category, related_name='estates')
    created_date = models.DateTimeField(default=now, editable=False)
    

    def get_price_per_meter(self):
        return f'{self.price / self.area} м²'

    def get_title(self):
        return self.title if self.title else f'{self.area} м², {self.room_amount} комнат'

    def __str__(self):
        return self.get_title()


class Photo(models.Model):
    img = models.ImageField()
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='photos')