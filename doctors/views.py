from django.shortcuts import render
from django.views.generic import ListView

from doctors.models import Doctor


class DoctorList(ListView):
    model = Doctor


def hospital(request):
    return render(request, "doctors/hospital.html")


def compain(request):
    return render(request, "doctors/compain.html")
