from django.contrib import admin
from orgApp import models

# Register your models here.

admin.site.register(models.Country)
admin.site.register(models.City)
admin.site.register(models.District)
admin.site.register(models.Thana)
admin.site.register(models.Organisation)
admin.site.register(models.Category)
admin.site.register(models.OrgDetail)
admin.site.register(models.OrgProject)
