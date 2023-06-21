from django.db import models
from django.contrib.auth.models import User

class user_info(models.Model):
    username=models.ForeignKey(User , on_delete=models.CASCADE)
    email=models.EmailField(max_length=150)
    password=models.CharField(max_length=30)
