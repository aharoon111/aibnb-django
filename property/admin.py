from django.contrib import admin
from . models import Property, Property_image, Category, Property_review, Property_Book
# Register your models here.


admin.site.register(Property)
admin.site.register(Property_image)
admin.site.register(Category)
admin.site.register(Property_review)
admin.site.register(Property_Book)
