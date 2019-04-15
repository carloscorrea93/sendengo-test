from django.contrib import admin
import core.models


class CarrierAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'owner_name', 'status')


class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'status', 'licence_type', 'carrier')


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'license_plate', 'status', 'type', 'carrier')


admin.site.register(core.models.Shipper)
admin.site.register(core.models.ShipperRequirement)
admin.site.register(core.models.Carrier, CarrierAdmin)
admin.site.register(core.models.CarrierLegalCompliance)
admin.site.register(core.models.Vehicle, VehicleAdmin)
admin.site.register(core.models.VehicleEquipment)
admin.site.register(core.models.Driver, DriverAdmin)
admin.site.register(core.models.DriverRequirement)
admin.site.register(core.models.Requirement)


