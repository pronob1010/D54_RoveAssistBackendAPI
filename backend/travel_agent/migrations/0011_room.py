# Generated by Django 3.2.8 on 2021-11-07 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel_agent', '0010_delete_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='hotel/room')),
                ('type', models.CharField(choices=[('single', 'Single'), ('double', 'Double')], max_length=15, null=True)),
                ('facilities', models.TextField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField(blank=True, null=True)),
                ('booked_by', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('rel_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='root_hotels', to='travel_agent.companyhotel')),
            ],
        ),
    ]
