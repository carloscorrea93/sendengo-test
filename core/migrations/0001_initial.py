# Generated by Django 2.2 on 2019-04-15 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=256)),
                ('owner_name', models.CharField(max_length=256)),
                ('owner_surname', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=512)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=254)),
                ('status', models.IntegerField(choices=[(0, 'Por validar'), (1, 'Validada'), (2, 'Suspendida')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CarrierLegalCompliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DriverRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=512)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ShipperRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('required_by', models.IntegerField(choices=[(0, 'Línea de transporte'), (1, 'Vehículo'), (2, 'Operador')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=8)),
                ('make', models.IntegerField()),
                ('model', models.IntegerField()),
                ('year', models.SmallIntegerField()),
                ('type', models.IntegerField(choices=[(0, 'Sin especificar'), (1, 'Camioneta de 1.5 toneladas'), (2, 'Camioneta de 3.5 toneladas'), (3, 'Camioneta de 5.5 toneladas'), (4, 'Rabón con caja seca'), (5, 'Rabón con caja refrigerada'), (6, 'Torton con caja seca'), (7, 'Torton con caja refrigerada'), (9, 'Trailer de 48ft con caja seca'), (10, 'Trailer de 48ft con caja refrigerada'), (11, 'Trailer de 53ft con caja seca'), (12, 'Trailer de 53ft con caja refrigerada')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Por validar'), (1, 'Validado'), (2, 'Suspendido')], default=0)),
                ('carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='core.Carrier')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('licence_type', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], default='A', max_length=1)),
                ('license_number', models.CharField(max_length=20)),
                ('license_expiration', models.DateField()),
                ('status', models.IntegerField(choices=[(0, 'Por validar'), (1, 'Validado'), (2, 'Suspendido')], default=0)),
                ('carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to='core.Carrier')),
            ],
        ),
    ]
