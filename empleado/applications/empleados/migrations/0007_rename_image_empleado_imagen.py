# Generated by Django 5.1.3 on 2025-01-03 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0006_empleado_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='image',
            new_name='imagen',
        ),
    ]
