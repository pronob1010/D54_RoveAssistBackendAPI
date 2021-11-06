# Generated by Django 3.2.8 on 2021-11-06 20:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel_agent', '0005_auto_20211107_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='booked_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]