# Generated by Django 5.0.2 on 2024-03-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounting', '0004_alter_invoice_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='service_name',
            field=models.CharField(choices=[('Consultation', 'Consultation'), ('X-Ray', 'X-Ray'), ('Blood Test', 'Blood Test'), ('Admit', 'Admit'), ('Medications', 'Medications'), ('ticket', 'ticket')], default='ticket', max_length=200),
        ),
    ]