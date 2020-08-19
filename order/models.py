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
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(null=True,blank = True)
    grade = models.CharField( choices = Grade_choices,max_length=20)
    types = models.CharField( choices = Type_choices,max_length=20 )

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
    status = models.CharField(choices = Status_Choices,max_length=20)

    def __str__(self):
        return self.orderid

class orderedcart(models.Model):
    pid = models.ForeignKey('product' , on_delete=models.SET_NULL, null=True, blank=True)
    orderedid = models.ForeignKey('orders' , on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.FloatField()
    pidtotal = models.FloatField()
