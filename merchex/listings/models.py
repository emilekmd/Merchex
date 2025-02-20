from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Band(models.Model):
    name = models.CharField(max_length=100)
    
    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROKC = 'AR'
        GOSPEL = "GP"

    genre = models.CharField(choices=Genre.choices,max_length=5)
    biography = models.CharField(max_length=1000)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900),MaxValueValidator(2025)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True,blank=True)
    
    # like_new = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.name}'
    
class Listing(models.Model):
    title = models.CharField(max_length=100)
    decription = models.CharField(max_length=250)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(validators=[MinValueValidator(0)],null=True,blank=True)
    
    class Type(models.TextChoices):
        Records="RC"
        CLothing="CL"
        Posters="PT"
        Miscellaneous="MC"
        
    type_e = models.CharField(choices=Type.choices,max_length=5)
    band = models.ForeignKey(Band,null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.title}'