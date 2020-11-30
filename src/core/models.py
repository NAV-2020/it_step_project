from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    """User`s post model"""
    
    title=models.CharField(max_length=45)
    body=models.TextField()
    image = models.ForeignKey('common.Photo', 
                            on_delete=models.CASCADE, 
                            null=True, 
                            blank=True)

    is_active = models.BooleanField(default=True)

    poster=models.ForeignKey(User,
                            on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.poster}: {self.title}'


