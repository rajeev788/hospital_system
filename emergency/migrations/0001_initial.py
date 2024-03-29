# Generated by Django 5.0.3 on 2024-03-10 04:48

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencySituation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PatientTriage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('triage_level', models.CharField(choices=[('Immediate', 'Immediate'), ('Delayed', 'Delayed'), ('Minor', 'Minor')], default='Immediate', max_length=200)),
                ('notes', models.TextField(blank=True)),
                ('emergency_situation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergency.emergencysituation')),
            ],
        ),
    ]
