from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Doctor, Specialization


class DoctorModelAdmin(ModelAdmin):
    model = Doctor
    menu_label = 'Doctors'  # ditch this to use verbose_name_plural from model
    menu_icon = 'group'  # change as required
    list_display = ('name', 'specialization')
    search_fields = ('name', 'specialization')


class SpecializationModelAdmin(ModelAdmin):
    model = Specialization
    menu_label = 'Specializations'  # ditch this to use verbose_name_plural from model
    menu_icon = 'tag'  # change as required
    list_display = ('specialization', )
    search_fields = ('specialization', )


modeladmin_register(DoctorModelAdmin)
modeladmin_register(SpecializationModelAdmin)
