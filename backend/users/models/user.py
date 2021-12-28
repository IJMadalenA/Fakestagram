# Django imported.
from django.db import models

# Create your models here.


class User(models.Model):
	class UserGender(models.TextChoices):
		MLE = 'Male'
		FLE = 'Female'
		SBN = 'Subnormal'
		
	class AccountStatus(models.TextChoices):
		ACT = 'Active'
		DCT = 'Deactivate'
		
	status = models.CharField(
		max_length=10,
		choices=AccountStatus.choices,
		default=AccountStatus.ACT
	)
	username = models.CharField(
		max_length=32,
		null=False,
		blank=False,
		unique=True,
	)
	first_name = models.CharField(
		max_length=32,
		null=True,
		blank=True,
	)
	last_name = models.CharField(
		max_length=32,
		null=True,
		blank=True,
	)
	birthdate = models.DateField(
		null=False,
		blank=False,
		auto_now=False,
	)
	country = models.CharField(
		max_length=32,
		null=True,
		blank=True,
	)
	gender = models.CharField(
		null=True,
		blank=True,
		choices=UserGender
	)
	creation_date = models.DateField(
		auto_now=True,
		editable=False,
		blank=False,
		null=False,
	)
