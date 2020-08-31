from django.db import models

class education(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.title 
         


class home(models.Model):
    title=models.CharField(max_length=100)
    heading = models.TextField( blank=True)
    description=models.TextField()
    image= models.ImageField(upload_to='portfolio/images/' , blank=True)
    def __str__(self):
        return self.title 


class experience(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.title 



class achievements(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()              
    def __str__(self):
        return self.title 


class contact(models.Model):
    title=models.CharField(max_length=100)
    address=models.TextField()
    phone=models.TextField(blank=True)
    email=models.TextField(blank=True)
    def __str__(self):
        return self.title 


class students(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image= models.ImageField(upload_to='portfolio/images/' , blank=True)
    def __str__(self):
        return self.name 
