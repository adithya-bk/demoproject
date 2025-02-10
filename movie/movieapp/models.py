from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=20)
    description = models.TextField()
    language = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images")
    year = models.IntegerField()

    def __str__(self):
        return self.title