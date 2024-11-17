from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.DoctorPatientTransaltor.index, name="homePage"),
    path("dptm/", include("DoctorPatient.dptm_urls")),
    path("about/", views.DoctorPatientTransaltor.aboutPage, name="aboutPage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)