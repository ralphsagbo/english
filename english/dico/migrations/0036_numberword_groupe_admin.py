# Generated by Django 2.1.5 on 2019-03-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dico', '0035_numberword_passgroupe'),
    ]

    operations = [
        migrations.AddField(
            model_name='numberword',
            name='groupe_admin',
            field=models.BooleanField(default=False),
        ),
    ]