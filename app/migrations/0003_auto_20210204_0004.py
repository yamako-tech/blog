# Generated by Django 2.2.18 on 2021-02-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postimage',
            field=models.ImageField(upload_to='media', verbose_name='postimage'),
        ),
    ]