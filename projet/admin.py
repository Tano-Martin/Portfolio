from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nom", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]


@admin.register(models.Imageprojet)
class ImageprojetAdmin(admin.ModelAdmin):
    list_display = ("view_image", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]

    def view_image(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="height:100px; width:120px">'
        )

    view_image.short_description = "Apercu de view_image"


@admin.register(models.Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = (
        "view_image",
        "nom",
        "url",
        "dateProjet",
        "client",
        "technologie",
        "date_add",
        "date_update",
        "status",
    )
    radio_fields = {"categorie": admin.VERTICAL}
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]

    def view_image(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="height:100px; width:120px">'
        )

    view_image.short_description = "Apercu de view_image"


@admin.register(models.Fait)
class FaitAdmin(admin.ModelAdmin):
    list_display = ("titre", "nombre", "icone", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["nombre", "status"]


@admin.register(models.Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ("view_photo", "nom", "poste", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]

    def view_photo(self, obj):
        return mark_safe(
            f'<img src="{obj.photo.url}" style="height:100px; width:120px">'
        )

    view_photo.short_description = "Apercu de view_photo"


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("titre", "icone", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]
