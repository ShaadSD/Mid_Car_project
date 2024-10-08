from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    title = models.CharField(max_length=50, default='Untitled')

    description = models.TextField(default='No description available.') 
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00) 
    photo = models.ImageField(upload_to="cars", default='path/to/default/image.jpg')
    quantity=models.IntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



    def __str__(self):
        return self.car_name

class Buy(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    car=models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"