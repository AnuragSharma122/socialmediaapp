from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=500)
    image = models.ImageField(upload_to='uploads/', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.content

    def number_of_likes(self):
        return self.likes.count()
