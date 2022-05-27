from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField('name', max_length=255)
    email = models.EmailField('Email ', max_length=255)
    address = models.TextField('address')
    message = models.TextField('Собщение')
    sent_at = models.DateField(auto_now_add=True)



class Userdata(models.Model):
    name = models.CharField('name', max_length=255)
    email = models.EmailField('Email ', max_length=255)
    address = models.TextField('address')
    message = models.TextField('Собщение')
    sent_at = models.DateField(auto_now_add=True)
