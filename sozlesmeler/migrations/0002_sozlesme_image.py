# Generated by Django 3.2 on 2021-04-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sozlesmeler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sozlesme',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Sözleşme dosyası'),
        ),
    ]