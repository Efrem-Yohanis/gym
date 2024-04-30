from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.GymMember)
admin.site.register(models.Plan)

