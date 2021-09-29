from django.shortcuts import get_object_or_404, render
from projet import models as models_projet
from . import models as models_siteweb

import re
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    siteweb = models_siteweb.Siteweb.objects.filter(status=True).first()
    configuration = models_siteweb.Configuration.objects.filter(status=True).first()
    apropos = models_siteweb.Apropos.objects.filter(status=True).first()
    travaux = models_siteweb.Travail.objects.filter(status=True)
    sociaux = models_siteweb.Reseauxsocial.objects.filter(status=True)
    certificats = models_siteweb.Certificat.objects.filter(status=True)
    resumes = models_siteweb.Resume.objects.filter(status=True)
    competences = models_siteweb.Competence.objects.filter(status=True)

    categories = models_projet.Categorie.objects.filter(status=True)
    imageprojets = models_projet.Imageprojet.objects.filter(status=True)
    projets = models_projet.Projet.objects.filter(status=True)
    faits = models_projet.Fait.objects.filter(status=True)
    temoignages = models_projet.Temoignage.objects.filter(status=True)
    services = models_projet.Service.objects.filter(status=True)

    return render(request, "index.html", locals())


def portfolioDetail(request, id_projet):
    projet = get_object_or_404(models_projet.Projet, id=id_projet)
    return render(request, "portfolio-details.html", locals())


def is_email(email):
    try:
        validate_email(email)
        return True
    except:
        return False


@csrf_exempt
def contactPost(request):
    success = True
    test_message = ""
    if request.method == "POST":
        email = json.loads(request.POST.get("email"))
        nom = json.loads(request.POST.get("nom"))
        sujet = json.loads(request.POST.get("sujet"))
        message = json.loads(request.POST.get("message"))

        if (
            email.isspace()
            or email == ""
            or sujet.isspace()
            or sujet == ""
            or nom.isspace()
            or nom == ""
            or message.isspace()
            or message == ""
        ):
            success = False
            test_message = "Veuillez remplir les champs vides, s'il vous plaît !"
        elif is_email(email):
            success = False
            test_message = "Veuillez saisir un email valide !"
        elif not re.fullmatch("[A-Za-z'éèëöüïäû ]+", nom):
            success = False
            test_message = "Veuillez saisir un nom valide !"
        else:
            contact, created = models_siteweb.Contact.objects.get_or_create(
                nom=nom, sujet=sujet, message=message, email=email
            )
            contact.save()
            if created:
                test_message = "Votre message a bien été envoyé !"
            else:
                test_message = "Votre message est déjà envoyé !"

    datas = {"success": success, "test_message": test_message}

    return JsonResponse(datas, safe=False)
