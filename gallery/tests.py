from django.test import TestCase
from .models import *

# Create your tests here.
class TestImage(TestCase):
    
    def setUp(self):
        self.lagos = Location.objects.create(name='Lagos')
        self.scenery = Category.objects.create(name='scenery')
        self.hotels = Category.objects.create(name='hotels')

        self.office = Image.objects.create(
            name='office', location=self.lagos,  description='an office picture')

        self.office.category.add(self.scenery)
        self.office.category.add(self.hotels)

    def test_instance(self):
        self.office.save()
        self.assertTrue(isinstance(self.office, Image)) 

    def test_delete_image(self):
        self.office.save()
        self.office.delete()
        self.assertTrue(len(Image.objects.all()) == 0) 

    def test_update(self):
        self.office.save()
        self.office.name = 'update_office'
        self.assertTrue(self.office.name == 'update_office') 

    def test_all_images(self):
        self.office.save()
        images = Image.all_images()
        self.assertTrue(len(images) > 0)    

    def test_show_by_category(self):
        self.office.save()
        cat = Category.objects.filter(name='scenery')
        images = Image.show_by_category(cat)
        self.assertTrue(len(images) > 0) 

    def test_view_location(self):
        self.office.save()
        location = Image.show_by_location(self.lagos)
        self.assertTrue(len(location) > 0)                
