# Generated by Django 2.1.5 on 2020-04-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20200425_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title_image',
            field=models.ImageField(default='default_title.jpg', upload_to='Article_heading_pics'),
        ),
    ]
