# Generated by Django 4.2.6 on 2023-11-09 16:07

from pickle import TRUE
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]