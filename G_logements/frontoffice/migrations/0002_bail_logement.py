# Generated by Django 3.2 on 2021-04-30 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontoffice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('loyerTTC', models.FloatField()),
                ('date_debut', models.DateField(auto_now_add=True)),
                ('duree', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Logement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbPieces', models.IntegerField()),
                ('surface', models.FloatField()),
                ('photo', models.CharField(max_length=200)),
                ('loyer', models.FloatField()),
                ('charges', models.FloatField()),
                ('partAgence', models.FloatField()),
            ],
        ),
    ]
