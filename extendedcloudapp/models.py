from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class Login(AbstractUser):
    is_dataowner = models.BooleanField(default=False)
    is_datareceiver = models.BooleanField(default=False)


class Owner(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='dataowner')
    Name = models.CharField(max_length=200)
    Contact_No = PhoneNumberField(unique=True, null=False, blank=False)
    Email = models.EmailField()
    Address = models.TextField(max_length=200)

    def __str__(self):
        return self.Name


class Receiver(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='datareceiver')
    Name = models.CharField(max_length=200)
    Contact_No = PhoneNumberField(unique=True, null=False, blank=False)
    Email = models.EmailField()
    Address = models.TextField(max_length=200)

    def __str__(self):
        return self.Name


class Upload(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Files = models.FileField(upload_to='', unique=True)


class Request(models.Model):
    User = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    File_Name = models.CharField(max_length=100)
    Message = models.TextField()
    Status = models.IntegerField(default=0)


    def __str__(self):
        return self.Name


class Download(models.Model):
    dec_key= models.CharField(max_length=1000, null=True, blank=True)
