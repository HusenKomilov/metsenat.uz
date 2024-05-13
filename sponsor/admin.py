from django.contrib import admin
from sponsor import models

admin.site.register(models.Organization)
admin.site.register(models.University)
admin.site.register(models.Sponsor)
admin.site.register(models.Student)
admin.site.register(models.StudentSponsor)
