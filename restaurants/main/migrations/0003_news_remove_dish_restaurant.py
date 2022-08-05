# Generated by Django 4.0.6 on 2022-08-05 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_adminuser_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('article', models.CharField(max_length=255)),
                ('time_posted', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='images/news/')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.RemoveField(
            model_name='dish',
            name='restaurant',
        ),
    ]
