from django.db import models
from django.utils.translation import ugettext_lazy as _



class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        s = str(self.name)
        return s

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=40)
    image = models.ImageField()
    links = models.CharField(max_length=500)
    description = models.CharField(max_length=40)


    transitcarname = models.ForeignKey(Category,null=False, verbose_name=_('Category'),
                                       on_delete=models.CASCADE)

    def __str__(self):
        return self.title