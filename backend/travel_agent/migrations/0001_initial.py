# Generated by Django 3.2.8 on 2021-11-06 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_review', models.BooleanField(default=False)),
                ('on_hold', models.BooleanField(default=False)),
                ('suspended', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='root_agent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_logo', models.ImageField(upload_to='company/logo')),
                ('primary_background', models.ImageField(blank=True, null=True, upload_to='company/background')),
                ('short_description', models.TextField(blank=True, max_length=200, null=True)),
                ('company_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company_root', to='travel_agent.agent')),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='company/post_image')),
                ('location', models.CharField(choices=[('Chattogram', 'Chattogram'), ('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna'), ('Barishal', 'Barishal'), ('Sylhet', 'Sylhet'), ('Dhaka', 'Dhaka'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh')], max_length=15, null=True)),
                ('host_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='root_host', to='travel_agent.companyinfo')),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='hotel/room')),
                ('type', models.CharField(choices=[('single', 'Single'), ('double', 'Double')], max_length=15, null=True)),
                ('facilities', models.TextField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField()),
                ('booked_by', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_root', to='travel_agent.hotel')),
            ],
        ),
    ]
