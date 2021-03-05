from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
class MyUserManager(BaseUserManager):
    def create_user(self, userPhoneNumber, password, **extra_fields):
        
        if not userPhoneNumber:
            raise ValueError('Users must have an phone number')

        user = self.model(
            userPhoneNumber=userPhoneNumber,
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, userPhoneNumber, password, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        extra_fields.setdefault('userRole', "admin")
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        #if extra_fields.get('is_staff') is not True:
         #   raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(userPhoneNumber, password, **extra_fields)


class User(AbstractBaseUser):
    USER_ROLES = (
        ("patient", "patient"),
        ("doctor", "doctor"),
        ("chamber", "chamber"),
        ("pathology", "pathology"),
        ("admin", "admin")
    )
    userId = models.AutoField(primary_key=True)
    userPhoneNumber = models.CharField(max_length=22, unique = True)
    userName = models.CharField(max_length=55)
    userRole = models.CharField(max_length=22, choices= USER_ROLES)
    #is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = MyUserManager()

    username = None
    USERNAME_FIELD = 'userPhoneNumber'
    

    def __int__(self):
        return self.userId

    def has_perm(self, perm, obj=None):
       "Does the user have a specific permission?"
       # Simplest possible answer: Yes, always
       return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser
   

   

    