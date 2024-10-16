# Generated by Django 5.1.2 on 2024-10-16 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventoapp', '0003_evento'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='lugar',
            name='detalleLugar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='tipoEvento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventoapp.tipoevento'),
        ),
    ]
