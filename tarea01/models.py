from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    #logo = models.ImageField(upload_to=photo_path, blank=True)
    code = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
	name = models.CharField(max_length=200)
	nickname = models.CharField(max_length=50)
	birthday = models.DateField() 
	age = models.IntegerField()
	rut = models.CharField(max_length=15)
	email = models.EmailField()
	#height = models.DecimalField() #estatura DEBE TENER max_digits
	#weight = models.DecimalField() #peso DEBE TENER max_digits
	#photo = models.ImageField(upload_to=photo_path, blank=True)
	#position 

	def __str__(self):
		return self.name


class Coach(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	email = models.EmailField()
	rut = models.CharField(max_length=15)
	nickname = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class SoccerGame(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name