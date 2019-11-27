from django.contrib.auth.models import User
from django.db import models

# Create your models here.

TYPES = [
    ('FUN', 'Fundacja'),
    ('ORG', 'Organizacja pozarządowa'),
    ('LOK', 'Zbiórka lokalna'),
]


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(choices=TYPES, default='FU', max_length=3)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    pick_up_datetime = models.DateTimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)



