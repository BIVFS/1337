from django.db import models

class Owners(models.Model):
	id = models.AutoField(primary_key=True)
	sname = models.CharField(max_length=20)
	fname = models.CharField(max_length=20)
	patr = models.CharField(max_length=20)
	sp = models.IntegerField()
	np = models.IntegerField()
	ph = models.IntegerField()

class Rooms(models.Model):
	id = models.AutoField(primary_key=True)
	square = models.IntegerField()
	address = models.CharField(max_length=30)

class Agreements(models.Model):
	id = models.AutoField(primary_key=True)
	dateConc = models.CharField(max_length=20)
	expDate = models.CharField(max_length=20)
	sname = models.CharField(max_length=20)
	fname = models.CharField(max_length=20)
	patr = models.CharField(max_length=20)
	address = models.CharField(max_length=30)