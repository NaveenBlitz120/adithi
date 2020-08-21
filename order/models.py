from django.db import models

# Create your models here.
class product(models.Model):
    Grade_choices = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
    )
    Type_choices = (
        ('count','count'),
        ('kg','kg'),
        ('grams','grams'),
    )
    category = (
        ('fruits','fruits'),
        ('vegetables','vegetables'),
        ('groceries','groceries'),
    )
    name = models.CharField(max_length=200)
    our_price = models.FloatField()
    market_price = models.FloatField()
    image = models.ImageField(null=True,blank = True)
    grade = models.CharField( choices = Grade_choices,max_length=20)
    types = models.CharField( choices = Type_choices,max_length=20 )
    category = models.CharField( choices = category,max_length = 60 )
    def __str__(self):
        return self.name

class orders(models.Model):
    Status_Choices = (
        ('pending' , 'pending'),
        ('orderconfiremd' , 'orderconfiremd'),
        ('cancelled' , 'cancelled'),
        ('completed' , 'completed'),
    )
    orderid = models.CharField(max_length = 10)
    phoneno = models.CharField(max_length = 10)
    name = models.CharField(max_length = 30)
    address = models.TextField()
    ordertotal = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(choices = Status_Choices,max_length=20,default = Status_Choices[0][0])
    offer = models.IntegerField(default=0)
    orderfinaltotal = models.FloatField(default = 0)
    def __str__(self):
        return self.orderid

class orderedcart(models.Model):
    pid = models.ForeignKey('product' , on_delete=models.SET_NULL, null=True, blank=True)
    orderedid = models.ForeignKey('orders' , on_delete=models.SET_NULL, null=True, blank=True)
    quantity_type = models.CharField(max_length=30,null=True)
    quantity = models.FloatField()
    pidtotal = models.FloatField()

class setcart(models.Model):
    minimum_cart_value = models.FloatField()
    silveroff_value = models.FloatField()
    goldenoff_value = models.FloatField()
    platinumoff_value = models.FloatField()
    silveroff_percentage = models.IntegerField()
    goldenoff_percentage = models.IntegerField()
    platinumoff_percentage = models.IntegerField()
