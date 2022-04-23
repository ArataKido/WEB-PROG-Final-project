from django import forms
from django.db import models

class ContactUs(models.Model):
    name= models.CharField(max_length=32)
    phone = models.CharField('Phone', max_length = 20)
    email = models.CharField('Email', max_length = 50)
    message= models.CharField('Message', max_length = 20)


    def __str__(self) :
        return '{} {} {} {}'.format(self.name, self.phone, self.email, self.message)

    class Meta:
        verbose_name="Contact Us"
        verbose_name_plural="Contact Us"

