from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(default='media/default_image.jpeg', upload_to='product', blank=False, null=False)
    description = models.TextField()

    def __str__(self):
        return self.title