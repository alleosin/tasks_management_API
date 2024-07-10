from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    patronymic = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150, unique=True)


class Customer(Profile):
    pass


class Worker(Profile):
    pass
