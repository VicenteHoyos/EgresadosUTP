# Generated by Django 3.0.5 on 2020-05-03 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20200502_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='interes',
        ),
        migrations.AddField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(to='posts.Interes'),
        ),
    ]
