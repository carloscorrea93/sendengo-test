from django.urls import path
from . import views

urlpatterns = [
    path('shippers/<int:shipper_id>/available_carriers/', views.available_carriers, name='available_carriers'),
]