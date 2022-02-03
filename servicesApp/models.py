from django.db import models

class Services(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    # indicates the name of the object in the db
    class Meta():
        verbose_name = 'service'
        verbose_name_plural = 'services'
        
        def __str__(self):
            return self.title
