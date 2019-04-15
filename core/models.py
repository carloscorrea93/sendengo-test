from django.db import models
import core.choices


class Shipper(models.Model):
    company_name = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=254)

    def __str__(self):
        return self.company_name


class ShipperRequirement(models.Model):
    name = models.TextField()
    required_by = models.IntegerField(choices=core.choices.SHIPPEER_REQUIREMENTS_CHOICES, default=0)

    def __str__(self):
        return self.name


class Carrier(models.Model):
    company_name = models.CharField(max_length=256)
    owner_name = models.CharField(max_length=256)
    owner_surname = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=254)
    status = models.IntegerField(choices=core.choices.STATUS_CHOICES, default=0)

    def __str__(self):
        return '%s [%s]' % (self.company_name, self.owner_name)


class CarrierLegalCompliance(models.Model):
    name = models.TextField()


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=8)
    make = models.IntegerField()
    model = models.IntegerField()
    year = models.SmallIntegerField()
    type = models.IntegerField(choices=core.choices.VEHICLE_TYPE, default=0)
    status = models.IntegerField(choices=core.choices.VEHICLE_DRIVER_STATUS_CHOICES, default=0)
    carrier = models.ForeignKey(Carrier, related_name='vehicles', on_delete=models.CASCADE)

    def __str__(self):
        return self.license_plate


class VehicleEquipment(models.Model):
    name = models.TextField()


class Driver(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    licence_type = models.CharField(max_length=1, choices=core.choices.LICENSE_TYPE_CHOICES, default='A')
    license_number = models.CharField(max_length=20)
    license_expiration = models.DateField()
    status = models.IntegerField(choices=core.choices.VEHICLE_DRIVER_STATUS_CHOICES, default=0)
    carrier = models.ForeignKey(Carrier, related_name='drivers', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.name, self.surname)


class DriverRequirement(models.Model):
    name = models.TextField()
