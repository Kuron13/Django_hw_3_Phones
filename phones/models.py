from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.URLField(null=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)
