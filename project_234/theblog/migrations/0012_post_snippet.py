# Generated by Django 4.0.1 on 2022-03-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0011_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='pera nai chill', max_length=255),
        ),
    ]