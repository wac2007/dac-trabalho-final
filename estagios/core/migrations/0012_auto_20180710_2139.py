# Generated by Django 2.0.6 on 2018-07-11 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_student_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='core.Skill', verbose_name='Habilidades'),
        ),
    ]
