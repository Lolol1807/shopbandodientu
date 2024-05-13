from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug= models.SlugField(max_length=200)
    def __str__(self):
        return(self.name)
class Product(models.Model):
    name= models.CharField(max_length=100,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    img=models.ImageField(upload_to="media/")
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    def __str__(self):
        return(self.name)