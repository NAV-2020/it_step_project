from django.contrib.auth.models import AbstractUser
from django.db import models


class RolesData:
    """Roles values for Role model"""
    DEFAULT = 1
    MANAGER = 2
    ADMIN = 5

    ROLES_CHOICES = (
        (DEFAULT, 'user'),
        (MANAGER, 'manager'),
        (ADMIN, 'admin')
    )


class Role(models.Model):
    """Management roles for users"""

    id = models.PositiveSmallIntegerField(choices=RolesData.ROLES_CHOICES,
                                          primary_key=True)

    @classmethod
    def get_default_user_role(cls):
        role, created = cls.objects.get_or_create(id=RolesData.DEFAULT)
        return role.id

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    """Custom User model"""
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username


class Profile(models.Model):
    first_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45, null=True, blank=True)

    avatar = models.OneToOneField('common.Photo', 
                                on_delete=models.CASCADE, 
                                null=True, 
                                blank=True)
    user = models.OneToOneField('User',
                                on_delete=models.CASCADE,
                                null=True)
    role = models.ForeignKey('Role',
                             default=Role.get_default_user_role,
                             on_delete=models.DO_NOTHING)

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name} | {self.role}"
        return f"{self.user.username} | {self.role}"