from django.db import models
from datetime import datetime
from django.conf import settings
#from django.db.models import models
from django.contrib.auth.models import User
import requests

# Create your models here.
class NotesModel(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	SrNo = models.AutoField(primary_key=True)
	title = models.CharField(max_length=20,blank=False)
	deadline = models.DateField(blank=False,default = datetime.now)
	description = models.TextField(blank=False)
	
	'''def task(SrNo,title,deadline,description):
		self.SrNo = SrNo
		self.title = title
		self.deadline = deadline
		self.description = description'''
	
		
	def __str__(self):
		return self.title