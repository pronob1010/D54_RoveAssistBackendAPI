# Generated by Django 3.2.8 on 2021-11-15 16:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagetour',
            name='entry',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
