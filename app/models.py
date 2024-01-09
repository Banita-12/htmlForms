from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    sloc=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    email=models.EmailField(default='abc@gmail.com')
    reenteremail=models.EmailField(default='abc@gmail.com')

    def __str__(self):
        return self.sname
