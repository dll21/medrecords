# Generated by Django 2.0.7 on 2018-07-15 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medrecords_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='height',
            field=models.FloatField(blank=True, null=True, verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='weight',
            field=models.IntegerField(verbose_name='Peso'),
        ),
    ]
