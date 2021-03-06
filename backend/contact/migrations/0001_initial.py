# Generated by Django 4.0.4 on 2022-05-12 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=20)),
                ('typecontact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.typecontact')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle')),
            ],
        ),
    ]
