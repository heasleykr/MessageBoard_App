from django.db import models

# Create your models here. Models are Objects
class Post(models.Model):
    text = models.TextField() #specified TYPE of content var will hold. 

    # add this to method to apps for readability 
    # method to return the STRING of the object, NOT the location in memory
    def __str__(self):
        return self.text[:50] #only display the first 50 characters. This is a 'slice'.
