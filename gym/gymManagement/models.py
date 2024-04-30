import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class gymAdmin(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)

class Plan(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    createdAt=models.DateTimeField(default=datetime.datetime.today())


    def __str__(self) -> str:
        return self.title + " " + str(self.price)

class GymMember(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=14,default='0900000000')
    photo=models.ImageField(upload_to='upload/profile',blank=True,null=True)
    plan=models.ForeignKey(Plan,on_delete=models.SET_NULL,null=True,blank=True)
    joinedAt=models.DateField(default=datetime.date.today())
    paidAt=models.DateTimeField(default=datetime.datetime.today())
    active=models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.firstName + " " + self.lastName




    
