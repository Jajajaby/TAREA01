from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='media')
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
	height = models.DecimalField(max_digits=4, decimal_places=2, default=0) #estatura 
	weight = models.DecimalField(max_digits=4, decimal_places=2, default=0) #peso 
	photo = models.ImageField(upload_to='media')
	POSITIONS_CHOICES = (
		('BASE', 'Base'),
		('ESCOLTA', 'Escolta'),
		('ALERO', 'Alero'),
		('ALA_PIVOT', 'Ala-pivot'),
		('PIVOT', 'Pivot'),
	)
	position = models.CharField(
		max_length=15,
        choices=POSITIONS_CHOICES)

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

#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
