# Generated by Django 2.1.5 on 2019-03-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dico', '0033_auto_20190307_1244'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profil',
        ),
        migrations.AddField(
            model_name='score',
            name='username',
            field=models.CharField(default='Z', max_length=100),
            preserve_default=False,
        ),
    ]
