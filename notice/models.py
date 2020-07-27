from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Branch(models.Model):
	name=models.CharField(max_length=100,default='')
	def __str__(self):
		return self.name

class Profile(models.Model):
	user=models.OneToOneField(to=User,on_delete=CASCADE)
	name=models.CharField(max_length=100)
	branch=models.ForeignKey(to=Branch,on_delete=CASCADE,null=True,blank=True)
	def __str__(self):
		return self.name



class Notice(models.Model):
	title=models.CharField(max_length=100,default='')
	description=models.TextField(default='')
	date=models.DateTimeField(auto_now_add=True)
	branch=models.ForeignKey(to=Branch,on_delete=CASCADE,null=True,blank=True)

