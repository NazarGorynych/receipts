# Generated by Django 4.0.6 on 2022-08-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0001_initial'),
        ('preferences', '0004_alter_orderingpreference_receipts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderingpreference',
            name='receipts',
            field=models.ManyToManyField(blank=True, related_name='receipts', to='receipts.receipt'),
        ),
    ]
