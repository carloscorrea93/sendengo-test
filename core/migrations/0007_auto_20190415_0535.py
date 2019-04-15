# Generated by Django 2.2 on 2019-04-15 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190415_0524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrierlegalcompliance',
            old_name='requirement_id',
            new_name='requirement',
        ),
        migrations.RenameField(
            model_name='driverrequirement',
            old_name='requirement_id',
            new_name='requirement',
        ),
        migrations.RenameField(
            model_name='vehicleequipment',
            old_name='requirement_id',
            new_name='requirement',
        ),
        migrations.AddField(
            model_name='carrierlegalcompliance',
            name='carrier',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Carrier'),
        ),
        migrations.AddField(
            model_name='driverrequirement',
            name='driver',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Driver'),
        ),
        migrations.AddField(
            model_name='vehicleequipment',
            name='vehicle',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Vehicle'),
        ),
    ]