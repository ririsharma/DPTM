from django.urls import path
from . import views

urlpatterns = [
    path("", views.DoctorPatientTransaltor.dptmHomePage, name="index"),
    path("translate_diagnostics/", views.DoctorPatientTransaltor.diagnosticsPage, name="translateDiagnostics"),
    path("translate_prescription/", views.DoctorPatientTransaltor.prescriptionsPage, name="translatePrescription"),
]