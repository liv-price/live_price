# Generated by Django 3.1.2 on 2020-10-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('model_number', models.CharField(max_length=60)),
                ('identification_number', models.CharField(max_length=50, unique=True)),
                ('site', models.CharField(max_length=50)),
                ('update_date', models.DateTimeField(verbose_name='Last Updated')),
                ('details', models.TextField(verbose_name='Product Details')),
            ],
        ),
    ]