# Generated by Django 2.1.5 on 2019-03-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dico', '0030_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='password2',
            field=models.CharField(max_length=50, null=True),
        ),
    ]