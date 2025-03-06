# Generated by Django 5.1.3 on 2025-03-05 13:32

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('nombre', models.CharField(max_length=255)),
                ('caracteristicas', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre completo')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('fecha', models.DateField(verbose_name='Fecha de reservación')),
                ('hora', models.TimeField(verbose_name='Hora de reservación')),
                ('num_personas', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de personas')),
                ('mensaje', models.TextField(blank=True, verbose_name='Mensaje adicional')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Reservación',
                'verbose_name_plural': 'Reservaciones',
                'ordering': ['-fecha', '-hora'],
            },
        ),
        migrations.CreateModel(
            name='Sugerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('section_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('sesion_id', models.CharField(blank=True, max_length=100, null=True)),
                ('total', models.DecimalField(decimal_places=0, max_digits=10)),
                ('metodo_pago', models.CharField(choices=[('nequi', 'Nequi'), ('bancolombia', 'Bancolombia')], max_length=20)),
                ('pagado', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ordenitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.IntegerField(default=1)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='web.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.producto')),
            ],
        ),
        migrations.CreateModel(
            name='carritoitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('sesion_id', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.producto')),
            ],
        ),
    ]
