# Generated by Django 2.0.5 on 2018-06-08 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_detiknewsitem_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detiknewsitem',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
