from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class DoctorPatientTransaltor:
    def __init__(self):
        pass

    def index(request):
        return render(request, "home/index.html")

    def aboutPage(request):
        return render(request, "about/index.html")

    def dptmHomePage(request):
        return render(request, "dptm.html")

    def prescriptionsPage(request):
        return render(request, "prescriptions/index.html")

    def diagnosticsPage(request):
        return render(request, "diagnostics/index.html")
