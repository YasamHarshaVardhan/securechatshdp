# Generated by Django 5.1.4 on 2024-12-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='U1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg1', models.CharField(max_length=450)),
            ],
        ),
        migrations.CreateModel(
            name='U2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg2', models.CharField(max_length=450)),
            ],
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
