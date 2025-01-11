from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Address)
admin.site.register(models.CouncilWorker)
admin.site.register(models.PropertyProfile)
admin.site.register(models.TenantProfile)
