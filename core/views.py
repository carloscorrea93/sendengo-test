from django.http import HttpResponse, Http404
from core.models import Shipper,Carrier


def available_carriers(request, shipper_id):
    try:
        shipper = Shipper.objects.get(pk=shipper_id)
        # get shipper requirments
        carrier_requirements = list(shipper.requirements.all().filter(type=0).values_list('id', flat=True))
        vehicle_requirements = list(shipper.requirements.all().filter(type=1).values_list('id', flat=True))
        driver_requirements = list(shipper.requirements.all().filter(type=2).values_list('id', flat=True))

        # get all carriers with status 1 and with less 1 driver and 1 vehicle
        carriers = Carrier.objects.all().distinct().filter(status=1, drivers__isnull=False, vehicles__isnull=False,
                                                           drivers__status=1, vehicles__status=1)
        if carrier_requirements:
            carriers_with_legal_requirements = carriers.\
                filter(requirements__carrier_requirement__pk__in=carrier_requirements)
        else:
            carriers_with_legal_requirements = carriers

        if vehicle_requirements:
            carriers_with_vehicle_requirements = carriers_with_legal_requirements\
                .filter(vehicles__requirements__vehicle_requirement__pk__in=vehicle_requirements)
        else:
            carriers_with_vehicle_requirements = carriers_with_legal_requirements

        if driver_requirements:
            carriers_with_driver_requirements = carriers_with_vehicle_requirements.\
                filter(drivers__requirements__driver_requirement__pk__in=driver_requirements)
        else:
            carriers_with_driver_requirements = carriers_with_vehicle_requirements

        carries_with_all_request = carriers_with_driver_requirements

    except Shipper.DoesNotExist:
        raise Http404("Shipper does not exist")
    return HttpResponse("You're looking at question %s." % shipper.company_name)
