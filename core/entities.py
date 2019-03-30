from django.db import models
from .models import *

class Farmer(models.Model):
	"""docstring for Farmer"""
	email = models.ForeignKey(MyUser, on_delete= models.CASCADE)
	username = models.CharField(max_length = 20)
	date_of_birth = models.DateField()
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'

	def __str__(self):
		return

class SalesOutlet(models.Model):
	"""docstring for SalesOutlet"""
	email = models.ForeignKey(MyUser, on_delete= models.CASCADE)
	username = models.CharField(max_length = 20)
	date_of_birth = models.DateField()
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'

	def __str__(self):
		return

class QA_Lab(models.Model):
	"""docstring for QA_Lab"""
	email = models.ForeignKey(MyUser, on_delete= models.CASCADE)
	username = models.CharField(max_length = 20)
	license_no= models.CharField(max_length = 20, unique=True)
	license_exp_date= models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	current_station_of_work= models.CharField(max_length=100)
	date_of_birth = models.DateField()
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'

	def __str__(self):
		return
		


class VetMedicineDistributer(models.Model):
	email = models.ForeignKey(MyUser, on_delete= models.CASCADE)
	username = models.CharField(max_length = 20)
	license_no= models.CharField(max_length = 20, unique=True)
	license_exp_date= models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	current_station_of_work= models.CharField(max_length=100)
	date_of_birth = models.DateField()
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'

	def __str__(self):
		return 