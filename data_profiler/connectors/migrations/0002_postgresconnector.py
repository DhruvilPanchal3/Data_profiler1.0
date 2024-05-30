# Generated by Django 4.2.11 on 2024-04-15 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connectors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostgresConnector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(default='PostgreSQL')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
