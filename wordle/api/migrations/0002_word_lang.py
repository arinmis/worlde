# Generated by Django 4.0.6 on 2022-07-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='lang',
            field=models.CharField(choices=[('tr', 'Turkish'), ('en', 'English')], default='en', max_length=2),
            preserve_default=False,
        ),
    ]
