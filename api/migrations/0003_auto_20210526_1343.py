# Generated by Django 3.2.3 on 2021-05-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_transaction_number_of_trip_left'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='finish_data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='start_data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
