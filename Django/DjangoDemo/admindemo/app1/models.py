from django.db import models

# Create your models here.
class Publisher(models.Model):
	id = models.AutoField(primary_key = True) 
	name = models.CharField(max_length = 64,null = False,unique = True)
	addr = models.CharField(max_length = 128)

	def __str__(self):
		return "<Publisher Object:{}>".format(self.name)

class Book(models.Model):
	id = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 64,null = False,unique = True)
	publisher = models.ForeignKey(to = "Publisher",on_delete=models.CASCADE)

	def __str__(self):
		return "<Book Object:{}>".format(self.title)

class Author(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 16,null = False,unique = True)
	book = models.ManyToManyField(to = "Book")

	def __str__(self):
		return "<Author OBject:{}>".format(self.name)

		