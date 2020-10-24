from django.contrib.auth.models import AbstractUser
from django.db import models


class Roles:
    """Roles data class"""
    DEFAULT = 1
    MANAGER = 2
    ADMIN = 5

    @staticmethod
    def get_default_user_role()->int:
        """Returns default role for user"""
        return Role.objects.get_or_create(id=Roles.DEFAULT)[0].id

class Role(models.Model):
    """Manage roles for users"""
    ROLES_CHOICES = (
        (Roles.DEFAULT, 'user'),
        (Roles.MANAGER, 'manager'),
        (Roles.ADMIN, 'admin')
    )

    id = models.PositiveSmallIntegerField(choices=ROLES_CHOICES,
                                            primary_key=True)

    def __str__(self):
        return self.get_id_display()

class User(AbstractUser):
    """Custom user model"""
    phone_number = models.CharField(max_length=13)
    role = models.ForeignKey(Role, 
                            default=Roles.get_default_user_role(),
                            on_delete=models.CASCADE)


    