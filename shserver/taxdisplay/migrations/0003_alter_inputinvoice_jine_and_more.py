# Generated by Django 4.2 on 2024-12-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxdisplay', '0002_inputinvoice_outputinvoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputinvoice',
            name='jine',
            field=models.DecimalField(decimal_places=4, max_digits=15, verbose_name='金额'),
        ),
        migrations.AlterField(
            model_name='inputinvoice',
            name='piaomianshuie',
            field=models.DecimalField(decimal_places=4, max_digits=15, verbose_name='票面税额'),
        ),
        migrations.AlterField(
            model_name='outputinvoice',
            name='jine',
            field=models.DecimalField(decimal_places=4, max_digits=15, verbose_name='金额'),
        ),
        migrations.AlterField(
            model_name='outputinvoice',
            name='piaomianshuie',
            field=models.DecimalField(decimal_places=4, max_digits=15, verbose_name='票面税额'),
        ),
    ]