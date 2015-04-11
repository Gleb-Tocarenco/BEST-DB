from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
	class Meta:
			db_table = 'auth_user'



class CompanyTypes(models.Model):
	name = models.CharField(max_length=255)



class Company(models.Model):
	name = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	company_type = models.ForeignKey(CompanyTypes)



class Event(models.Model):
	name = models.CharField(max_length=255)
	start = models.DateField()
	end = models.DateField()



class Call(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey(Event)
	company = models.ForeignKey(Company)
	date = models.DateTimeField()


class Material(models.Model):
	name = models.CharField(max_length=255)
	filename = models.FileField(max_length=100)

