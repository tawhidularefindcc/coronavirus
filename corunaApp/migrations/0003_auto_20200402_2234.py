# Generated by Django 3.0.4 on 2020-04-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corunaApp', '0002_auto_20200402_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]