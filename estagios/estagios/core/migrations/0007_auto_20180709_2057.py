# Generated by Django 2.0.6 on 2018-07-09 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180709_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=48, verbose_name='Título')),
            ],
            options={
                'verbose_name': 'competência',
                'verbose_name_plural': 'competências',
            },
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(to='core.Skill'),
        ),
    ]
