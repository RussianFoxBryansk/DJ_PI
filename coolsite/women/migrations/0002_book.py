# Generated by Django 4.2.5 on 2023-11-20 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_book', models.CharField(max_length=50, verbose_name='Наименование книги')),
                ('avtor', models.CharField(max_length=25, verbose_name='Автор')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
