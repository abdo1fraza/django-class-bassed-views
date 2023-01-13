from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 1000)
    created_at = models.DateField(default = timezone.now)
    image = models.ImageField(upload_to='posts_image/')### make folder posts_image in media folder and store images in it 


    def __str__(self):
        return str(self.title)



