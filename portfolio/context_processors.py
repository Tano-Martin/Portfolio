from siteweb import models as models_siteweb


def data(request):
    siteweb = models_siteweb.Siteweb.objects.filter(status=True).first()
    configuration = models_siteweb.Configuration.objects.filter(status=True).first()
    return locals()
