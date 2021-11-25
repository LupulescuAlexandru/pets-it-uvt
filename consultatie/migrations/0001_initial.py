# Generated by Django 2.1.7 on 2021-11-25 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0002_auto_20211125_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='consultatie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataconsultatie', models.DateField(null=True, verbose_name='Dată consultație')),
                ('oraconsultatie', models.TimeField(null=True, verbose_name='Oră consultație')),
                ('tratamente', models.TextField(max_length=1000, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal')),
            ],
            options={
                'verbose_name': 'Consultație',
                'verbose_name_plural': 'Consultații',
            },
        ),
    ]