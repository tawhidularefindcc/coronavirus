from django.db import models


class Users(models.Model):
    user_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    password_one = models.CharField(max_length=100)
    password_two = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name
