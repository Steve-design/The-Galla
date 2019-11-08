from django.db import models
from tinymce.models import HTMLField

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
              