from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel

class Doctor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    specialization = models.ForeignKey('Specialization', related_name='doctors', on_delete=models.PROTECT)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    governorate = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    clinic_address = models.CharField(max_length=1024, blank=True)
    clinic_phone = models.CharField(max_length=64, blank=True)
    openning = models.TimeField(null=True)
    closing = models.TimeField(null=True)


    panels = [
        FieldPanel('name'),
        FieldPanel('specialization'),
        ImageChooserPanel('photo'),
        FieldPanel('governorate'),
        FieldPanel('city'),
        FieldPanel('clinic_address'),
        FieldPanel('clinic_phone'),
        FieldPanel('openning'),
        FieldPanel('closing'),
    ]
    def __str__(self):
        return self.name


class Specialization(models.Model):
    specialization = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.specialization
