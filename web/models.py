from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name_category = models.CharField(max_length=256)

    def __str__(self):
        return self.name_category


class Transaction(models.Model):
    transaction_date = models.DateTimeField()
    type_of_transaction = models.CharField(max_length=256)
    amount = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Task(models.Model):
    creation_date = models.DateTimeField()
    status = models.CharField(max_length=256)
    task_name = models.CharField(max_length=256)
    task_description = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
