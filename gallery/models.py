from django.db import models
from tinymce.models import HTMLField
from fontawesome.fields import IconField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    @classmethod
    def all_locations(cls):
        locations=cls.objects.all()
        return locations

    class Meta:
        ordering = ['name']   

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name  

    @classmethod
    def all_categories(cls):
        categories=cls.objects.all()
        return categories
    

class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=30)
    description = HTMLField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)  

    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images  

    @classmethod
    def show_by_category(cls, category):
        images = cls.objects.filter(category=category)
        return images              

    @classmethod
    def show_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images        