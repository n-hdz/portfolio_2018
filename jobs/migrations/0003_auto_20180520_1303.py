# Generated by Django 2.0.2 on 2018-05-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='img/jobs', verbose_name='thumbnail'),
        ),
    ]