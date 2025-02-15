# Generated by Django 4.2.18 on 2025-02-04 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_driver', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('ride_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('ongoing', 'Ongoing'), ('completed', 'Completed')], max_length=20)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drives', to='rides.user')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rides', to='rides.user')),
            ],
        ),
    ]
