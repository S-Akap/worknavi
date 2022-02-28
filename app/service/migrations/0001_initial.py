# Generated by Django 4.0.2 on 2022-02-17 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registered_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=3)),
                ('age', models.IntegerField()),
                ('requirement', models.CharField(blank=True, max_length=30, null=True)),
                ('hourly_pay', models.IntegerField(blank=True, null=True)),
                ('citizenship', models.CharField(blank=True, max_length=25, null=True)),
                ('residence', models.CharField(blank=True, max_length=100, null=True)),
                ('is_contact', models.BooleanField()),
            ],
        ),
    ]
