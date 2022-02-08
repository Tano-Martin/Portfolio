from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(models.Siteweb)
class SitewebAdmin(admin.ModelAdmin):
    list_display = (
        "view_photoProfil",
        "view_photoCouverture",
        "nom",
        "prenom",
        "email",
        "telephone",
        "adresse",
        "date_add",
        "date_update",
        "status",
    )
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["email", "status"]

    def view_photoProfil(self, obj):
        return mark_safe(
            f'<img src="{obj.photoProfil.url}" style="height:100px; width:120px">'
        )

    view_photoProfil.short_description = "Apercu de view_photoProfil"

    def view_photoCouverture(self, obj):
        return mark_safe(
            f'<img src="{obj.photoCouverture.url}" style="height:100px; width:120px">'
        )

    view_photoCouverture.short_description = "Apercu de view_photoCouverture"


@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ("date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]


@admin.register(models.Apropos)
class AproposAdmin(admin.ModelAdmin):
    list_display = ("titre", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    filter_horizontal = ["option"]
    list_editable = ["status"]


@admin.register(models.Optionapropos)
class OptionaproposAdmin(admin.ModelAdmin):
    list_display = ("titre", "information", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["information", "status"]


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "sujet", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["email", "status"]


@admin.register(models.Travail)
class TravailAdmin(admin.ModelAdmin):
    list_display = ("liste", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]


@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("titre", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    filter_horizontal = ["option"]
    list_editable = ["status"]


@admin.register(models.Optionresume)
class OptionresumeAdmin(admin.ModelAdmin):
    list_display = (
        "titre",
        "nomStructure",
        "periode",
        "date_add",
        "date_update",
        "status",
    )
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["nomStructure", "status", "periode"]


@admin.register(models.Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ("titre", "pourcentage", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["pourcentage", "status"]


@admin.register(models.Certificat)
class CertificatAdmin(admin.ModelAdmin):
    list_display = ("view_image", "titre", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["titre", "status"]

    def view_image(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="height:100px; width:120px">'
        )

    view_image.short_description = "Apercu des images"


@admin.register(models.Socialicone)
class SocialiconeAdmin(admin.ModelAdmin):
    list_display = ("nom", "icone", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["icone", "status"]


@admin.register(models.Reseauxsocial)
class ReseauxsocialAdmin(admin.ModelAdmin):
    list_display = ("lien", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]
