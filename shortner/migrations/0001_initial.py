# Generated by Django 2.0.7 on 2018-08-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortify',
            fields=[
                ('longURL', models.CharField(max_length=900)),
                ('addDate', models.DateTimeField(auto_now_add=True)),
                ('autoIncrement', models.AutoField(primary_key=True, serialize=False)),
                ('shortURL', models.CharField(max_length=600)),
            ],
        ),
    ]
