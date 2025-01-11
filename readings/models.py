from django.db import models
from django.conf import settings


# Create your models here.
class TenantProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_tenant = models.BooleanField(default=True)

    def __str__(self):
        return f"Tenant(id{self.name}, {self.user.first_name} {self.user.last_name})"


class Address(models.Model):
    location = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    property_number = models.IntegerField()

    def __str__(self):
        return f"id={self.location}, {self.location} {self.street}"


class CouncilWorker(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"CWorker(id = {self.id}, name = {self.user.first_name} {self.user.last_name})"


class PropertyProfile(models.Model):
    tenant = models.ForeignKey(TenantProfile, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    monthly_reading = models.DecimalField(max_digits=12, decimal_places=2)
    date_recorded = models.DateField()
    reading_recorder = models.OneToOneField(CouncilWorker, on_delete=models.CASCADE)

    def __str__(self):
        return {self.tenant}
