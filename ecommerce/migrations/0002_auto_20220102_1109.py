# Generated by Django 3.2.10 on 2022-01-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='c_meta_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='c_meta_title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
