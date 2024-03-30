from django.db import models
from django.utils import slugify

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=50, unqiue=True)
    url = models.URLField()
    slug = models.SlugField()
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{ self.name } | { self.clicks }"
    
    def click(self):
        self.clicks += 1
        self.save()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        return super().save(*args, **kwargs)