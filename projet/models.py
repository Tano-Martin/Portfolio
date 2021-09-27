from django.db import models

# Create your models here.
class Categorie(models.Model):
	nom = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Categorie'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.nom

class Imageprojet(models.Model):
	image = models.FileField(upload_to='Imageprojet_file')
	projet = models.ForeignKey('projet.Projet', related_name='imageProjet', on_delete=models.CASCADE)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Imageprojet'
		verbose_name_plural = 'Imageprojets'

	def __str__(self):
		return f'{self.image}'

class Projet(models.Model):
	nom = models.CharField(max_length=255)
	description = models.TextField()
	image = models.FileField(upload_to='Projet_file')
	url = models.URLField()
	dateProjet = models.DateField()
	client = models.CharField(max_length=255)
	categorie = models.ForeignKey('projet.Categorie', related_name='categorieProjet', on_delete=models.CASCADE)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Projet'
		verbose_name_plural = 'Projets'

	def __str__(self):
		return self.nom

class Fait(models.Model):
	titre = models.CharField(max_length=255)
	nombre = models.IntegerField(default=0)
	icone = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Fait'
		verbose_name_plural = 'Faits'

	def __str__(self):
		return self.titre

class Temoignage(models.Model):
	nom = models.CharField(max_length=255)
	poste = models.CharField(max_length=255)
	photo = models.FileField(upload_to='Temoignage_file')
	temoignage = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Temoignage'
		verbose_name_plural = 'Temoignages'

	def __str__(self):
		return self.nom

class Service(models.Model):
	titre = models.CharField(max_length=255)
	icone = models.CharField(max_length=255)
	description = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Service'
		verbose_name_plural = 'Services'

	def __str__(self):
		return self.titre

