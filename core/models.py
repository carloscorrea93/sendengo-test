from django.db import models
import core.choices


class Shipper(models.Model):
    company_name = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=254)
    requirements = models.ManyToManyField('Requirement', through='ShipperRequirement', related_name='requirements',
                                          default=0)

    def __str__(self):
        return self.company_name


class Carrier(models.Model):
    company_name = models.CharField(max_length=256)
    owner_name = models.CharField(max_length=256)
    owner_surname = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=254)
    status = models.IntegerField(choices=core.choices.STATUS_CHOICES, default=0)
    requirements = models.ManyToManyField('Requirement', through='CarrierLegalCompliance',
                                          related_name='legal_requirements', default=0)

    def __str__(self):
        return '%s [%s]' % (self.company_name, self.owner_name)


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=8)
    make = models.IntegerField()
    model = models.IntegerField()
    year = models.SmallIntegerField()
    type = models.IntegerField(choices=core.choices.VEHICLE_TYPE, default=0)
    status = models.IntegerField(choices=core.choices.VEHICLE_DRIVER_STATUS_CHOICES, default=0)
    carrier = models.ForeignKey(Carrier, related_name='vehicles', on_delete=models.CASCADE)
    requirements = models.ManyToManyField('Requirement', through='VehicleEquipment',
                                          related_name='vehicle_requirements', default=0)

    def __str__(self):
        return self.license_plate


class Driver(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    licence_type = models.CharField(max_length=1, choices=core.choices.LICENSE_TYPE_CHOICES, default='A')
    license_number = models.CharField(max_length=20)
    license_expiration = models.DateField()
    status = models.IntegerField(choices=core.choices.VEHICLE_DRIVER_STATUS_CHOICES, default=0)
    carrier = models.ForeignKey(Carrier, related_name='drivers', on_delete=models.CASCADE)
    requirements = models.ManyToManyField('Requirement', through='DriverRequirement',
                                          related_name='driver_requirements', default=0)

    def __str__(self):
        return '%s %s' % (self.name, self.surname)


class Requirement(models.Model):
    name = models.TextField()
    type = models.IntegerField(choices=core.choices.SHIPPEER_REQUIREMENTS_CHOICES, default=0)

    def __str__(self):
        return '%s | %s' % (self.name, self.get_type_display())


class ShipperRequirement(models.Model):
    shipper = models.ForeignKey(Shipper, related_name='shipper', on_delete=models.CASCADE, default=0)
    requirement = models.ForeignKey(Requirement, related_name='requirement', on_delete=models.CASCADE,
                                    default=0)

    def __str__(self):
        return '%s %s' % (self.shipper, self.requirement)


class CarrierLegalCompliance(models.Model):
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE, default=0)
    requirement = models.ForeignKey(Requirement, related_name='carrier_requirement', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return '%s %s' % (self.carrier, self.requirement)


class VehicleEquipment(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=0)
    requirement = models.ForeignKey(Requirement, related_name='vehicle_requirement', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '%s %s' % (self.vehicle, self.requirement)


class DriverRequirement(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, default=0)
    requirement = models.ForeignKey(Requirement, related_name='driver_requirement', on_delete=models.CASCADE, default=2)

    def __str__(self):
        return '%s %s' % (self.driver, self.requirement)
