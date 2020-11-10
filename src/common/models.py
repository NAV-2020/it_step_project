from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='upload/images/')
    is_avatar = models.BooleanField(default=False)