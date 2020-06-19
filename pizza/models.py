from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Size(models.Model):
    title=models.CharField(max_length=100)


    def __str__(self):
        return self.title

class Pizza(models.Model):
    topping1 =models.CharField(max_length=100)
    topping2 =models.CharField(max_length=100)
    size =models.ForeignKey(Size,on_delete=models.CASCADE)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username

