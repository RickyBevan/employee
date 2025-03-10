

# Create your models here.


from django.db import models

class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age= models.IntegerField()
    

    def _str_(self):
       return self.name
