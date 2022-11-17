from django.http import HttpResponse ,JsonResponse
from django.shortcuts import render ,redirect
from .models import Firma, Degerlendirme, OgrenciBasvuru, OgrenciBilgi
from django.contrib.auth import authenticate,  login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from koustaj.forms import basvuruForm


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


# Create your views here.
def index(request):
    return HttpResponse("merhaba")

def anasayfa(request):
    return render(request, 'anasayfa.html')
   

def belge(request):
    degerlendirmes = Degerlendirme.objects.all()
    return render(request, 'belge.html',{'degerlendirmes':degerlendirmes})

def ogrenci(request):
    current_user = request.user
    id = current_user.id
    ogrencib = OgrenciBilgi.objects.raw("SELECT * FROM koustaj_ogrencibilgi WHERE id=%s",[id])
    return render(request, 'ogrenci.html',{'data':ogrencib} )

def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
                    
        user = authenticate(request, username = username, password = password)
        
        if user is not None :
            login(request, user)
         
            if len(username) == 9:
                return redirect('anasayfa.html')
            elif len(username) == 4:
                return redirect('belge.html')
        else:
            return render(request,'login.html',{"error":"kullanıcı no ya da parola yanlış"})
                                    
    return render(request, 'login.html')

def basvuru(request):
    bform = basvuruForm
    return render(request,'basvuru.html', {'bform':bform})

def saveform(request):
    bform = basvuruForm(request.POST)
    bform.save()
    return HttpResponse('basvuru eklendi')

def export_pdf(request):

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)
    p.drawString(100,100,"Hello World!")
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
   
    
def nott(request):
    firmas = Firma.objects.all()
    return render(request, 'nott.html',{'firmas':firmas} )

def anasayfaOgretmen(request):
    return render(request, 'anasayfaOgretmen.html')

def basvurularOgretmen(request):
    return render(request, 'basvurularOgretmen.html')

def kbasvurular(request):
    return render(request, 'kbasvurular.html')

def kbasvurulistele(request):
    return render(request, 'kbasvurulistele.html')

def kullanıcı(request):
    return render(request, 'kullanıcı.html')

def sifre(request):
    return render(request, 'sifre.html')
    