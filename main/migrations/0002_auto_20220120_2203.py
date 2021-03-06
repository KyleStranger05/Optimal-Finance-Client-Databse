# Generated by Django 3.2 on 2022-01-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyclass',
            name='BuildingName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='BuildingNo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='CellNumber',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='City',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='CompanyName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='ContactPerson',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='EmailAddress',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='OfficeNumber',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='RefNo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='StreetName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='StreetNo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='Suburb',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companyclass',
            name='TaxRegNo',
            field=models.CharField(max_length=50),
        ),
    ]
