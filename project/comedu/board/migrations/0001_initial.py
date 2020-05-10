# Generated by Django 2.2 on 2020-05-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True, null=True)),
                ('genre', models.CharField(choices=[('C', 'C'), ('C++', 'C++'), ('Python', 'Python'), ('Javacript', 'Javascript'), ('R', 'R'), ('Others', 'Others'), ('Text', 'Text')], max_length=10)),
            ],
        ),
    ]
