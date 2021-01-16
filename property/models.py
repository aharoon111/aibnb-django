from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
from django.utils import timezone

# Create your models here.

class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    price = models.IntegerField("")
    description = models.TextField(max_length=1200)
    Place = models.TextField(max_length=50)
    image = models.ImageField(upload_to='Property_list/')
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    


    def __str__(self):
        return self.name


class Property_image(models.Model):
    property = models.ForeignKey('property', related_name='property_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Property_detail')

    def __str__(self):
        return str(self.proerty)

class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    title = models.CharField(max_length = 50)
    
    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return (self.title)


class Property_review(models.Model):
    user = models.ForeignKey(User, verbose_name=("review_auther"), on_delete=models.CASCADE)
    property = models.ForeignKey(Property,related_name = 'property_review', on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=1200)
    

    def __str__(self):
        return (self.property)

    class Meta:
        
        verbose_name = 'Property_review'
        verbose_name_plural = 'Property_reviews'



Count_Choices = (
    (1 , 1),
    (2 , 2),
    (3 , 3),
    (4 , 4),
    (5 , 5),
   )



class Property_Book(models.Model):
    """Model definition for Property_Book."""

    # TODO: Define fields here
    property = models.ForeignKey(Property,related_name = 'property_book', on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    from_Date = models.DateField(default=timezone.now)
    to_Date = models.DateField(default=timezone.now)
    children = models.IntegerField(choices= Count_Choices)
    guest = models.IntegerField(choices= Count_Choices)

    
    class Meta:
        """Meta definition for Property_Book."""

        verbose_name = 'Property_Book'
        verbose_name_plural = 'Property_Books'

    def __str__(self):
        """Unicode representation of Property_Book."""
        return (Property_Book.name)
