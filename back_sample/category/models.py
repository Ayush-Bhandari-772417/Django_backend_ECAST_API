from django.db import models
from django.utils.text import slugify
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)
    added_by = models.CharField(max_length=50)
    description = RichTextField(blank=False,null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,null=False,blank=False,editable=False)
    def __str__(self):
        return self.category
    
    def save(self, *args, **kwargs):
        slug_txt=f'{self.category}'
        self.slug = slugify(slug_txt)
        super(Category, self).save(*args, **kwargs)



