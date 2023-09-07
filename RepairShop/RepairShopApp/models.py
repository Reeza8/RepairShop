from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=150)

    def __str__(self):
        return str(self.user)


class Device(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    factor = models.TextField(blank=True)
    problem = models.CharField(max_length=100)
    point = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    status = models.BooleanField(default=False, blank=True)
    tracking_code = models.CharField(max_length=40, null=True)

    def __str__(self):
        return "{} from {}".format(self.name, self.customer.user.get_username())


# choice field class
class ThingPriority(models.IntegerChoices):
    process0 = 0, 'process1'
    process1 = 1, 'process2'
    process2 = 2, 'process3'
    process3 = 3, 'process4'
    process4 = 4, 'process5'


class Process(models.Model):
    name = models.IntegerField(default=0, choices=ThingPriority.choices)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    description = models.TextField()
    entry_date = models.DateField(auto_now_add=True)
    exit_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{} of {}".format(self.name, self.device.name)
