# Generated by Django 3.2.8 on 2021-11-06 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agent', '0002_alter_room_booked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='company_name',
            field=models.CharField(blank=True, max_length=156, null=True),
        ),
    ]
