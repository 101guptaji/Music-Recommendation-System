# Generated by Django 3.1.2 on 2020-10-23 02:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('songreviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
