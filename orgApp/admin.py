from django.contrib import admin
from orgApp import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(models.Country)

@admin.register(models.City,models.District,models.Thana)
class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.register(models.Organisation)
admin.site.register(models.Category)
admin.site.register(models.OrgDetail)
admin.site.register(models.OrgProject)


