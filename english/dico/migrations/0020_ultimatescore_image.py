# Generated by Django 2.1.5 on 2019-02-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dico', '0019_auto_20190204_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='ultimatescore',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]