# Generated by Django 2.1.5 on 2019-01-27 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dico', '0002_delete_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000)),
                ('mot', models.CharField(max_length=100)),
                ('commentaire', models.TextField(null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ultimate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WordTranslate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000)),
                ('mot_translate', models.CharField(max_length=100)),
                ('ultimate', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='translate_word',
            field=models.ManyToManyField(related_name='translate', to='dico.WordTranslate'),
        ),
    ]
