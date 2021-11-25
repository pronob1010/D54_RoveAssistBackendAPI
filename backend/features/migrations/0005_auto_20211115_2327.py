# Generated by Django 3.2.8 on 2021-11-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0004_alter_packagetour_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addplace',
            name='description',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='addplace',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='addrestaurant',
            name='description',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='addrestaurant',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='packagetour',
            name='description',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='packagetour',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]