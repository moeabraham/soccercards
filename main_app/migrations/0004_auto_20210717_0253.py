# Generated by Django 3.2.4 on 2021-07-17 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_fixture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fixture',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='team',
            name='cards',
            field=models.ManyToManyField(to='main_app.Card'),
        ),
    ]
