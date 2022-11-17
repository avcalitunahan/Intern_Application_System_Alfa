from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("index.html", views.index), 
    path("anasayfa.html", views.anasayfa ),
    path("belge.html", views.belge ),
    path("nott.html", views.nott),
    path("ogrenci.html", views.ogrenci ),
    path("login", views.login_request, name="login"),
    path("anasayfaOgretmen.html", views.anasayfaOgretmen ),
    path("basvurularOgretmen.html", views.basvurularOgretmen ),
    path("kbasvurular.html", views.kbasvurular),
    path("kbasvurulistele.html", views.kbasvurulistele),
    path("kullanıcı.html", views.kullanıcı ),
    path("sifre.html", views.sifre),
    path('form', views.basvuru),
    path('save',views.saveform),
    path('export_pdf', views.export_pdf, name="export-pdf")
    
    
]
