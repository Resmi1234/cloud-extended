from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class Login(AbstractUser):
    is_dataowner = models.BooleanField(default=False)
    is_datareceiver = models.BooleanField(default=False)

class Owner(models.Model):
    User = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='dataowner')
    Name = models.CharField(max_length=200)
    Contact_No = PhoneNumberField(unique=True, null=False, blank=False)
    Email = models.EmailField()
    Address = models.TextField(max_length=200)

    def __str__(self):
        return self.Name

class Receiver(models.Model):
    User = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='datareceiver')
    Name = models.CharField(max_length=200)
    Contact_No = PhoneNumberField(unique=True, null=False, blank=False)
    Email = models.EmailField()
    Address = models.TextField(max_length=200)

    def __str__(self):
        return self.Name

# class Document(models.Model):
    # docfile = models.FileField(upload_to='documents/%Y/%m/%d')



class Upload(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Files = models.FileField(unique=True)


