# Generated by Django 4.2.4 on 2024-04-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=200)),
                ('patient_father_name', models.CharField(max_length=200)),
                ('booked_date', models.DateField(verbose_name='date booked')),
            ],
        ),
    ]