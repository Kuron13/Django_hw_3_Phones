from django.db import models
from slugify import slugify

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)
    image = models.URLField(null=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, null=True)

    #def __str__(self):
    #    return self.name
    def save(self,  *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Phone, self).save(*args, **kwargs)
