from django.db import models

class ContactUs(models.Model):
    """This class saves data in database

    Args:
        models : is used to reffer to class models

    Returns:
        _str_: returns data in str format
    """
    name= models.CharField(max_length=32)
    phone = models.CharField('Phone', max_length = 20)
    email = models.CharField('Email', max_length = 50)
    message= models.CharField('Message', max_length = 20)


    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.phone, self.email, self.message)

    class Meta:
        #changes name of this model in db
        verbose_name="Contact Us"
        verbose_name_plural="Contact Us"

class Comments(models.Model):
    """This class saves data in database

    Args:
        models : is used to reffer to class models

    Returns:
        _str_: returns data in str format
    """

    name = models.CharField("Comments", max_length = 100)

    def __str__(self):
        return self.name
    
    class Meta:
        #changes name of this model in db
        verbose_name="Comment"
        verbose_name_plural="Comments"
