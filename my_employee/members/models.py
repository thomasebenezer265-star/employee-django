from django.db import models

# Create your models here.
class Employee(models.Model):

    employeename=models.CharField(max_length=200)

    
    department=models.CharField(max_length=200)

    age=models.IntegerField()

    

    address=models.CharField(max_length=200)

    def _str_(self):
        
        return self.employeename

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    address = models.TextField()
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.FloatField() 
