from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']