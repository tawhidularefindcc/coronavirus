# Generated by Django 3.0.4 on 2020-04-28 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgApp', '0006_auto_20200429_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgdetail',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orgdetail',
            name='org',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_detail', to='orgApp.Organisation'),
        ),
    ]
