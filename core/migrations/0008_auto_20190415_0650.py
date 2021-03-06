# Generated by Django 2.2 on 2019-04-15 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190415_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverrequirement',
            name='requirement',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.Requirement'),
        ),
        migrations.AlterField(
            model_name='shipperrequirement',
            name='requirement',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='requirement', to='core.Requirement'),
        ),
        migrations.AlterField(
            model_name='shipperrequirement',
            name='shipper',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='shipper', to='core.Shipper'),
        ),
        migrations.AlterField(
            model_name='vehicleequipment',
            name='requirement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Requirement'),
        ),
    ]
