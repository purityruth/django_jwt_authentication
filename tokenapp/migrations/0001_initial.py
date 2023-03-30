# Generated by Django 4.1.7 on 2023-03-30 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Organization_name', models.CharField(blank=True, max_length=300, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_users', models.CharField(blank=True, max_length=200, null=True)),
                ('expiration_date', models.DateTimeField()),
                ('parent_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tokenapp.organization')),
            ],
        ),
    ]
