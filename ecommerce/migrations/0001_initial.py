# Generated by Django 3.2.10 on 2022-01-02 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=250, unique=True)),
                ('c_email', models.CharField(max_length=250, unique=True)),
                ('c_email1', models.CharField(blank=True, max_length=250, null=True)),
                ('c_email2', models.CharField(blank=True, max_length=250, null=True)),
                ('c_phone', models.CharField(max_length=250)),
                ('c_phone1', models.CharField(blank=True, max_length=250, null=True)),
                ('c_phone2', models.CharField(blank=True, max_length=250, null=True)),
                ('c_address', models.CharField(max_length=250)),
                ('c_logo', models.ImageField(blank=True, null=True, upload_to='logo')),
            ],
        ),
    ]
