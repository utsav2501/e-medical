# Generated by Django 4.2.4 on 2024-04-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0003_record_delete_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='reguser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_email', models.CharField(max_length=200)),
                ('user_phone', models.CharField(max_length=200)),
            ],
        ),
    ]
