# Generated by Django 2.1.4 on 2019-02-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dico', '0014_remove_ultimatescore_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberword',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
