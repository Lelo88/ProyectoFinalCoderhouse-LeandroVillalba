# Generated by Django 4.1.3 on 2022-11-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]