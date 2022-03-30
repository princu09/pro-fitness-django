from django.db import models
from django.contrib.auth.models import User
import jsonfield

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250)
    desc = models.TextField()
    usage = models.TextField()
    price = models.IntegerField()
    categories = models.TextField()
    rating = models.IntegerField()
    images1 = models.ImageField(upload_to='')

    def __str__(self):
        return f"Id : {self.id}" " | " f"Title : {self.title}"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    itemLen = models.IntegerField(primary_key=False)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order Id {self.order_id}  : {self.update_desc[0:]}" + "..."

class Order(models.Model):
    id = models.IntegerField(primary_key=True, serialize=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=10)
    order_Items = jsonfield.JSONField()
    itemLen = jsonfield.JSONField()
    price = jsonfield.JSONField()
    amount = models.IntegerField(default=0)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=15)
    payment_method = models.CharField(max_length=15, default="COD")
    date = models.DateField(auto_now=True , auto_now_add=False)

    def __str__(self):
        return f"ID : {self.id} | Items : {self.order_Items}"
