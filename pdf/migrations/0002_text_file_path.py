# Generated by Django 4.1.4 on 2022-12-24 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='file_path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]