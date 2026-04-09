from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from .managers import ArticleManager

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(unique= True,blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)



    objects = ArticleManager()
    adminobjects = models.Manager()


    def __str__(self):
        return f"{self.slug} - {self.updated_date}"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)


    def delete(self,*args,**kwargs):
        self.is_deleted = True 
        self.save()

    def recover(self):
        self.is_deleted = False
        self.save()