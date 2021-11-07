# Generated by Django 3.2.8 on 2021-11-07 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agent', '0012_auto_20211108_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='company/post_image')),
                ('location', models.CharField(choices=[('Chattogram', 'Chattogram'), ('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna'), ('Barishal', 'Barishal'), ('Sylhet', 'Sylhet'), ('Dhaka', 'Dhaka'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh')], max_length=15, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='root_host', to='travel_agent.companyinfo')),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='rel_hotel',
        ),
        migrations.DeleteModel(
            name='companyHotel',
        ),
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='root_hotels', to='travel_agent.hotel'),
        ),
    ]