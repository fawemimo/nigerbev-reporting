# Generated by Django 4.0.6 on 2022-07-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pics',
            field=models.ImageField(default='default.png', upload_to='profile/pics'),
        ),
    ]