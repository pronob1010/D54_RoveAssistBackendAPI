# Generated by Django 3.2.8 on 2021-11-06 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('travel_agent', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='packageTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='company/post_image')),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('entry', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agent.agent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='addPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='company/post_image')),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
