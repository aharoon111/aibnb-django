from django.db import models

# Create your models here.

class about(models.Model):
    """Model definition for about."""

    # TODO: Define fields here
    image = models.ImageField(upload_to='about/')
    What_we_do = models.TextField(max_length=2000)
    mission = models.TextField(max_length=2000)
    Goals = models.TextField(max_length=2000)
    
    class Meta:
        """Meta definition for about."""

        verbose_name = 'about'
        verbose_name_plural = 'about'

    def __str__(self):
        """Unicode representation of about."""
        pass


class FAQ(models.Model):
    """Model definition for FAQ."""

    # TODO: Define fields here
    Title = models.CharField(max_length = 200)
    Description = models.TextField(max_length=2000)

    class Meta:
        """Meta definition for FAQ."""

        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        """Unicode representation of FAQ."""
        pass


