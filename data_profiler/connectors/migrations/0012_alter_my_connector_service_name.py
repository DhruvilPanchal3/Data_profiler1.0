# Generated by Django 4.2.11 on 2024-05-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectors', '0011_postgresconnector_database_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_connector',
            name='service_name',
            field=models.CharField(choices=[('mysql', 'MySQL'), ('postgres', 'PostgreSQL')], max_length=10),
        ),
    ]