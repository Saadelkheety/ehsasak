from django.urls import path

from doctors import views


urlpatterns = [
    path("doctors/", views.DoctorList.as_view(), name="doctors"),
    path("hospital/", views.hospital, name="hospital"),
    path("compain/", views.compain, name="compain"),
]
