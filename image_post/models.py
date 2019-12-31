from django.db import models

# Create your models here.
class ImagePost(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)
    post = models.ManyToManyField(ImagePost)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name
