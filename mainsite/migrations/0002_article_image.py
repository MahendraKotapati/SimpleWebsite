# Generated by Django 2.2.7 on 2020-04-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=12, upload_to=''),
            preserve_default=False,
        ),
    ]
