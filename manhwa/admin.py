from django.contrib import admin
from .models import reviews, Comment, Favourites
# Register your models here.
admin.site.register(reviews)
admin.site.register(Comment)
admin.site.register(Favourites)