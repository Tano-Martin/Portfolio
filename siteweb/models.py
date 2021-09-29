from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Siteweb(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    photoProfil = models.FileField(upload_to="Siteweb_file")
    photoCouverture = models.FileField(upload_to="Siteweb_file")
    telephone = models.CharField(max_length=255)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)
    localisation = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Siteweb"
        verbose_name_plural = "Sitewebs"

    def __str__(self):
        return self.nom


class Configuration(models.Model):
    descriptionAPropos = models.TextField()
    descriptionFait = models.TextField()
    descriptionCompetence = models.TextField()
    descriptionResume = models.TextField()
    descriptionDiplome = models.TextField(blank=True, null=True)
    descriptionPortfolio = models.TextField()
    descriptionService = models.TextField()
    descriptionTemoignage = models.TextField()
    descriptionContact = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    def __str__(self):
        return f"{self.descriptionAPropos}"


class Apropos(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    option = models.ManyToManyField(
        "siteweb.Optionapropos", related_name="detailApropos"
    )
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Apropos"
        verbose_name_plural = "Aproposs"

    def __str__(self):
        return self.titre


class Optionapropos(models.Model):
    titre = models.CharField(max_length=255)
    information = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Optionapropos"
        verbose_name_plural = "Optionaproposs"

    def __str__(self):
        return self.titre


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    sujet = models.CharField(max_length=255)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.nom


class Travail(models.Model):
    liste = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Travail"
        verbose_name_plural = "Travails"

    def __str__(self):
        return self.liste


class Resume(models.Model):
    titre = models.CharField(max_length=255)
    option = models.ManyToManyField("siteweb.Optionresume", related_name="optionResume")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self):
        return self.titre


class Optionresume(models.Model):
    titre = models.CharField(max_length=255)
    nomStructure = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    description = HTMLField(blank=True, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Optionresume"
        verbose_name_plural = "Optionresumes"

    def __str__(self):
        return self.titre


class Competence(models.Model):
    titre = models.CharField(max_length=255)
    pourcentage = models.IntegerField(default=0)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Competence"
        verbose_name_plural = "Competences"

    def __str__(self):
        return self.titre


class Certificat(models.Model):
    titre = models.CharField(max_length=255)
    image = models.FileField(upload_to="Certificat_file")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Certificat"
        verbose_name_plural = "Certificats"

    def __str__(self):
        return self.titre


class Socialicone(models.Model):
    nom = models.CharField(max_length=255)
    icone = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Socialicone"
        verbose_name_plural = "Socialicones"

    def __str__(self):
        return self.nom


class Reseauxsocial(models.Model):
    lien = models.CharField(max_length=255)
    sociaux = models.ForeignKey(
        "siteweb.Socialicone", related_name="social_icon", on_delete=models.CASCADE
    )
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Reseauxsocial"
        verbose_name_plural = "Reseauxsocials"

    def __str__(self):
        return self.lien
