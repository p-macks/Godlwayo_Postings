# Generated by Django 4.2.4 on 2023-09-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
