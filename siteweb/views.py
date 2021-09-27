from django.shortcuts import get_object_or_404, render
from projet import models as models_projet
from . import models as models_siteweb
import siteweb


# Create your views here.
def index(request):
    siteweb = models_siteweb.Siteweb.objects.filter(status=True).first()
    configuration = models_siteweb.Configuration.objects.filter(status=True).first()
    apropos = models_siteweb.Apropos.objects.filter(status=True).first()
    travaux = models_siteweb.Travail.objects.filter(status=True)
    sociaux = models_siteweb.Sociaux.objects.filter(status=True)
    diplomes = models_siteweb.Diplome.objects.filter(status=True)
    categoriePapiers = models_siteweb.Categoriepapier.objects.filter(status=True)
    resume = models_siteweb.Resume.objects.filter(status=True)
    optionresume = models_siteweb.Optionresume.objects.filter(status=True)
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
