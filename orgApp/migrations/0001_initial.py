# Generated by Django 3.0.4 on 2020-04-26 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('division', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('thana', models.CharField(max_length=255)),
                ('postal_area', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('org_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgApp.Category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='orgProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('duration', models.DateTimeField()),
                ('image', models.ImageField(upload_to='')),
                ('budget', models.CharField(max_length=255)),
                ('status', models.TextField(verbose_name='Status')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgApp.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='orgDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('logo', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('facebook_url', models.URLField()),
                ('twitter_url', models.URLField()),
                ('youtube_url', models.URLField()),
                ('website_url', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('org_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orgApp.Organisation')),
            ],
        ),
    ]
