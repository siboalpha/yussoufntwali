# Generated by Django 4.1.3 on 2022-11-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_youtubelink_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubelink',
            name='video_link',
            field=models.TextField(max_length=500),
        ),
    ]
