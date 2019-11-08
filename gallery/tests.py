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
