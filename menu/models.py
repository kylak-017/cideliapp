from django.db import models

# Create your models here.


#Each class represents a distinct field in the database
class User(models.Model):
    full_name = models.CharField(max_length=70) #(get user id as email)
    pass_word = models.CharField(max_length = 70)

    def username(self):
        return self.full_name
    def password(self):
        return self.pass_word


class Drink(models.Model):
    cost = models.IntegerField(default = 0)
    toppings = models.TextField(max_length = 70)
    imagePath = models.IntegerField(default = 0)
    hotorcold = ""

    temp = models.BooleanField(default = True)
    if(temp):
        hotorcold = "Hot"
    else:
        hotorcold = "Cold"


    def info(self):
        return "Cost:" + self.cost + "Hot Or Cold?:" + self.hotorcold + "Toppings:" + self.toppings

class Order(models.Model):
    ordered_user = models.ForeignKey(User, on_delete=models.CASCADE )
    ordered_drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def order_info(self):
        return "Great! Your order summary is as follows:\n" + "User ID:" + self.ordered_user + "\nOrdered Drink:" + self.ordered_drink  