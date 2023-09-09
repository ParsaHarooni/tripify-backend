from django.contrib import admin
from core import models

admin.site.register(models.Expense)
admin.site.register(models.Trip)