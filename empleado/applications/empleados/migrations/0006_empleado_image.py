# Generated by Django 5.1.3 on 2025-01-03 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_empleado_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/empleado'),
        ),
    ]