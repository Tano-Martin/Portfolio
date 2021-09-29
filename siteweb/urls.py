from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
	path('portfolio/<int:id_projet>', views.portfolioDetail, name="portfolioDetail"),
    path('contactPost', views.contactPost, name="contactPost"),

]

