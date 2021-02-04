from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('category', max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category =models.ForeignKey(Category, verbose_name='category', on_delete=models.PROTECT)
    title = models.CharField("title", max_length=200)
    image = models.ImageField(upload_to='images', verbose_name='postimage', null=True, blank=True)
    content = models.TextField("content")
    created = models.DateTimeField("created", default=timezone.now)
    

    def __str__(self):
        return self.title