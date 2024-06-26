from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    # upload_to = 'default directory'
    # default = 'default image for user profile'
    def __str__(self):
        return f'{self.user.username} Profile'






