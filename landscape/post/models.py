from django.db import models




class Post(models.Model):
    image = models.ImageField()
    description = models.CharField(max_length=100)


    def __str__(self):
        return self.description