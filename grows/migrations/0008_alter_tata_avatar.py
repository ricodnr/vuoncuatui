# Generated by Django 4.1.5 on 2023-02-11 14:03

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('grows', '0007_tata_fintime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tata',
            name='avatar',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
