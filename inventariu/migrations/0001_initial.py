# Generated by Django 2.1.7 on 2021-11-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumabile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nume', models.CharField(max_length=50)),
                ('cantitate', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Consumabil',
                'verbose_name_plural': 'Consumabile',
                'ordering': ('nume',),
            },
        ),
    ]
