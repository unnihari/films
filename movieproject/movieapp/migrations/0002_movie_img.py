# Generated by Django 4.2.5 on 2023-10-17 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='sssd', upload_to='gallary'),
            preserve_default=False,
        ),
    ]
