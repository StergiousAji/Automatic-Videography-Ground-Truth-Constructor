# Generated by Django 2.1.5 on 2023-03-25 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.BooleanField(default=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('filename', models.CharField(max_length=50)),
                ('transcript', models.TextField(null=True)),
                ('coverart_colour', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('_ground_truth', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Audio Sources',
            },
        ),
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True)),
                ('text', models.CharField(max_length=200)),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('_image_ids', models.CharField(max_length=500)),
                ('_selected_ids', models.CharField(max_length=500)),
                ('slug', models.SlugField()),
                ('audio', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ground_truth.Audio')),
            ],
            options={
                'verbose_name_plural': 'Chunks',
            },
        ),
    ]