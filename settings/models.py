from django.db import models

# Create your models here.
class Settings(models.Model):
    site_name = models.CharField(max_length = 150)
    logo = models.ImageField(upload_to='logo/')
    subtitle = models.TextField(max_length = 500)
    fb_link = models.URLField(max_length=200)
    tw_link = models.URLField(max_length=200)
    insta_link = models.URLField(max_length=200)
    place = models.CharField( max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    

    
    
    
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'