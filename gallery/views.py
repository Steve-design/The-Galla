from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def show_categories(request):
    # categories=Category.all_categories()
    locations = Location.objects.all()

    categories = Category.objects.all()
    images = Image.all_images()

    # imagescategory = Image.show_by_category(category=ca)


    if request.GET.get("category"):
        images = Image.show_by_category(request.GET.get("category"))

    elif request.GET.get("location"):
        images = Image.show_by_location(request.GET.get("location"))

    else:
        images= Image.all_images()



    # images = Image.objects.all()
    #
    # if request.GET.get("category")):
    #     images = Image.filter_by_category(request.GET.get("category"))

    return render(request, 'images/homepage.html', {"categories":categories,"locations":locations,  "images":images })

#
# def images(request):
#     images=Image.all_images()
#     return render (request, 'images/homepage.html', {"images":images})