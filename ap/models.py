from django.db import models
# Create your models here.

class Customer(models.Model):
    Name=models.CharField(max_length=200,null=True)
    Age=models.IntegerField(null=True)
    DateCreated=models.DateTimeField(auto_created=True,null=True)
    def __str__(self):
        return self.Name

class Tag(models.Model):
    Name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Name

class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    Name=models.CharField(max_length=200,null=True)
    Price=models.FloatField(null=True)
    Category=models.CharField(max_length=100,null=True,choices=CATEGORY)
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return self.Name

class Order(models.Model):

    STATUS=(
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered')
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=100,null=True,choices=STATUS)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)


