from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits.")], null=True)
    place = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
