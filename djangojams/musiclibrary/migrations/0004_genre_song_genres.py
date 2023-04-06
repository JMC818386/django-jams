# Generated by Django 4.2 on 2023-04-05 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclibrary', '0003_album_song_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='genres',
            field=models.ManyToManyField(null=True, to='musiclibrary.genre'),
        ),
    ]
