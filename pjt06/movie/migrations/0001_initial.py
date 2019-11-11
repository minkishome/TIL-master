# Generated by Django 2.2.6 on 2019-10-18 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('title_en', models.CharField(max_length=50)),
                ('audience', models.IntegerField()),
                ('open_date', models.DateField()),
                ('genre', models.CharField(max_length=30)),
                ('watch_grade', models.CharField(max_length=30)),
                ('score', models.FloatField()),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=150)),
                ('score', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
        ),
    ]