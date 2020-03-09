from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class StudentUserManager(BaseUserManager):
    def create_user(self,rollno,name,email,password=None):
        if not email:
            raise ValueError("User must have an email")
        if not name:
            raise ValueError("User must have a name")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.name = name
        user_obj.rollno = rollno
        user_obj.save(using=self._db)
        return user_obj

class StudentUser(AbstractBaseUser):
    rollno = models.IntegerField(default=0)
    name = models.CharField(max_length=100,default='')
    email = models.EmailField(max_length=255,unique=True,default='')
    active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    
    objects = StudentUserManager()

