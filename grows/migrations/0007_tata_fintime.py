# Generated by Django 4.1.5 on 2023-02-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grows', '0006_alter_tata_maxhumi_alter_tata_maxtemp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tata',
            name='fintime',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
