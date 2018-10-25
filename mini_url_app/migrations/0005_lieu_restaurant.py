# Generated by Django 2.0 on 2018-09-19 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mini_url_app', '0004_eleve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('lieu_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mini_url_app.Lieu')),
                ('menu', models.TextField()),
            ],
            bases=('mini_url_app.lieu',),
        ),
    ]