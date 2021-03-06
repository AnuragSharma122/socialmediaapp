from django.db import models
from django.contrib.auth.models import AbstractUser, User
from PIL import Image
from django.urls.base import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('userProfile', kwargs={'username': self.user})

    def __str__(self):
        return f'{self.user.username}'

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
