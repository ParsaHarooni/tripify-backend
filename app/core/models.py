from django.db import models
from django.contrib.auth.models import User


EXPENSE_CATEGORY = (
    ("SH", "Shopping"),
    ("F", "Food"),
    ("C", "Commute"),
    ("E", "Entertainment"),
    ("O", "Other")
)


class Trip(models.Model):
    city = models.CharField(verbose_name='city', max_length=128)
    country = models.CharField(verbose_name='country', max_length=128)
    owner = models.ForeignKey(verbose_name='owner', to=User, on_delete=models.CASCADE)
    people = models.IntegerField(verbose_name='people')
    
    def __str__(self) -> str:
        return f"{self.country} - {self.city} - {self.people}"
    
class Expense(models.Model):
    reason = models.CharField(verbose_name='reason', max_length=128)
    price = models.IntegerField(verbose_name='price')
    category = models.CharField(verbose_name='category', choices=EXPENSE_CATEGORY, max_length=2)
    trip = models.ForeignKey(verbose_name='trip', to=Trip, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.reason} - {self.reason}"