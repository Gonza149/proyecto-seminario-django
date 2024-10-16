# Generated by Django 5.1.2 on 2024-10-16 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventoapp', '0002_lugar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fechaEvento', models.DateField()),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventoapp.lugar')),
            ],
        ),
    ]
