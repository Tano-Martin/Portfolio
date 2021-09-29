from django.shortcuts import get_object_or_404, render
from projet import models as models_projet
from . import models as models_siteweb

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
    diplomes = models_siteweb.Diplome.objects.filter(status=True)
    categoriePapiers = models_siteweb.Categoriepapier.objects.filter(status=True)
    resumes = models_siteweb.Resume.objects.filter(status=True)
    competences = models_siteweb.Competence.objects.filter(status=True)

    contact = models_siteweb.Contact.objects.filter(status=True)

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
    messages = ""
    success = False
    if request.method == 'POST':
        # newEmail = json.loads(request.POST.get('email'))
        # if newEmail.isspace():
        #     messages = "Veuillez remplir ce champs avant de le soumettre !"
        # elif is_email(newEmail):
        #     messages = "Email invalide"
        # else:
        #     news, created = models_siteweb.Contact.objects.get_or_create(email=newEmail)
        #     news.save()
        #     if created:
        #         messages = "Email envoyé avec succès"
        #     else:
        #         messages = "Email déjà envoyé"
        #     success = True
        print("ENVOYEEEEEEEEEEEEEEEEE SUCCCCEE")
        messages = "Email envoyé avec succès"
    datas = {
        "success": success,
        "messages": messages
    }
    return JsonResponse(datas, safe=False)