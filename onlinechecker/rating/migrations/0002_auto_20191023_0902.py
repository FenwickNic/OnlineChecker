# Generated by Django 2.2.6 on 2019-10-22 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waverating',
            name='rating',
            field=models.IntegerField(choices=[(0, 'Bad'), (1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Excellent')]),
        ),
    ]
