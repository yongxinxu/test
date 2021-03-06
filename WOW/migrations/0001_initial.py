# Generated by Django 2.0.5 on 2018-05-22 15:55

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', ckeditor.fields.RichTextField()),
                ('files', models.FileField(upload_to='media/')),
                ('url', models.URLField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('attributes', models.TextField()),
            ],
        ),
    ]
