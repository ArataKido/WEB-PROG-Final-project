from django.db import models

class Name(models.Model):
    name= models.CharField('Name', max_length = 50)
    
    def __str__(self) :
        return self.name
        
class Phone(models.Model):
    phone = models.CharField('Phone', max_length = 20)
    
    def __str__(self) :
        return self.phone

class Email(models.Model):
    email = models.CharField('Email', max_length = 50)
    
    def __str__(self):
        return self.email


class Message(models.Model):
    message= models.CharField('Message', max_length = 20)
    
    def __str__(self) :
        return self.message 
