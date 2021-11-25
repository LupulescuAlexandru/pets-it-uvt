# Generated by Django 2.1.7 on 2021-11-25 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventariu', '0001_initial'),
        ('animal', '0002_auto_20211125_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumabileFisa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantitate', models.IntegerField(blank=True, null=True)),
                ('consumabile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventariu.Consumabile')),
            ],
            options={
                'verbose_name': 'Consumabile',
                'verbose_name_plural': 'Consumabile',
            },
        ),
        migrations.CreateModel(
            name='Fisa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(null=True)),
                ('apetit', models.CharField(blank=True, max_length=30, null=True)),
                ('consumulvoluntardeapa', models.CharField(blank=True, max_length=15, null=True, verbose_name='Consumul voluntar de apa')),
                ('prehensiunea', models.CharField(blank=True, max_length=30, null=True)),
                ('masticatia', models.CharField(blank=True, max_length=30, null=True)),
                ('deglutitia', models.CharField(blank=True, max_length=30, null=True)),
                ('voma', models.CharField(blank=True, max_length=30, null=True)),
                ('defecarea', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulcavitatiiorale', models.CharField(blank=True, max_length=30, null=True, verbose_name='Examenul cavitatii orale')),
                ('examenulcavitatiioraleother', models.TextField(blank=True, max_length=100, null=True)),
                ('examenulfaringului', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulfaringuluiother', models.TextField(blank=True, max_length=100, null=True)),
                ('examenulesofagului', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulesofaguluiother', models.TextField(blank=True, max_length=100, null=True)),
                ('examenulabdomenului', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulabdomenuluiother', models.TextField(blank=True, max_length=100, null=True)),
                ('examenulstomacului', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulstomaculuiother', models.TextField(blank=True, max_length=100, null=True)),
                ('examenulintestinelor', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulintestinelorother', models.TextField(blank=True, max_length=100, null=True)),
                ('examenulanusului', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulanusuluiother', models.TextField(blank=True, max_length=100, null=True)),
                ('examenulfecalelor', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulfecalelorother', models.TextField(blank=True, max_length=100, null=True)),
                ('eaxmenulglanexe', models.CharField(blank=True, max_length=30, null=True)),
                ('eaxmenulglanexeother', models.TextField(blank=True, max_length=100, null=True)),
                ('examenulglsalivare', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulglsalivareother', models.TextField(blank=True, max_length=100, null=True)),
                ('ariahepatica', models.CharField(blank=True, max_length=30, null=True)),
                ('ariapancreatica', models.CharField(blank=True, max_length=30, null=True)),
                ('tuse', models.CharField(blank=True, max_length=30, null=True)),
                ('jetaj', models.CharField(blank=True, max_length=30, null=True)),
                ('mirosulaparatuluiexpirat', models.CharField(blank=True, max_length=30, null=True)),
                ('mirosulaparatuluiexpiratother', models.TextField(blank=True, max_length=100, null=True)),
                ('cornaj', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulnasului', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulnasuluiother', models.TextField(blank=True, max_length=100, null=True)),
                ('examenulsinusului', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulsinusuluiother', models.TextField(blank=True, max_length=100, null=True)),
                ('examenullaringelui', models.CharField(blank=True, max_length=30, null=True)),
                ('examenullaringeluiother', models.TextField(blank=True, max_length=100, null=True)),
                ('examenultraheei', models.CharField(blank=True, max_length=30, null=True)),
                ('examenultraheeiother', models.TextField(blank=True, max_length=100, null=True)),
                ('tipulrespiraor', models.CharField(blank=True, max_length=30, null=True)),
                ('dispnee', models.CharField(blank=True, max_length=30, null=True)),
                ('murmurvezicular', models.CharField(blank=True, max_length=30, null=True)),
                ('raluriuscate', models.CharField(blank=True, max_length=30, null=True)),
                ('raluriumede', models.CharField(blank=True, max_length=30, null=True)),
                ('sufluri', models.TextField(blank=True, max_length=150, null=True)),
                ('sunetpercutie', models.CharField(blank=True, max_length=30, null=True)),
                ('sunetpercutieother', models.TextField(blank=True, max_length=150, null=True)),
                ('altemodificaritoraco2', models.TextField(blank=True, max_length=150, null=True)),
                ('dispneecardio', models.CharField(blank=True, max_length=30, null=True)),
                ('dispneecardioother', models.TextField(blank=True, max_length=150, null=True)),
                ('zgomotulcardiac', models.CharField(blank=True, max_length=30, null=True)),
                ('zgomotulcardiacother', models.TextField(blank=True, max_length=150, null=True)),
                ('altemodificaricardio', models.TextField(blank=True, max_length=150, null=True)),
                ('pulsul', models.CharField(blank=True, max_length=30, null=True)),
                ('mictiunea', models.CharField(blank=True, max_length=30, null=True)),
                ('sensibilitatea', models.CharField(blank=True, max_length=30, null=True)),
                ('marime', models.CharField(blank=True, max_length=30, null=True)),
                ('sensibilitateavezicii', models.CharField(blank=True, max_length=30, null=True)),
                ('graddeplentitudine', models.CharField(blank=True, max_length=30, null=True)),
                ('altemodificariurinar', models.TextField(blank=True, max_length=150, null=True)),
                ('schiopatura', models.CharField(blank=True, max_length=30, null=True)),
                ('schiopaturaother', models.TextField(blank=True, max_length=150, null=True)),
                ('aplomburi', models.CharField(blank=True, max_length=30, null=True)),
                ('tumefacatiiarticulare', models.CharField(blank=True, max_length=30, null=True)),
                ('mobilitatearticulara', models.CharField(blank=True, max_length=30, null=True)),
                ('durerearticulara', models.CharField(blank=True, max_length=30, null=True)),
                ('durerediafizara', models.CharField(blank=True, max_length=30, null=True)),
                ('deficitpropioceptiv', models.CharField(blank=True, max_length=30, null=True)),
                ('masamusculara', models.CharField(blank=True, max_length=30, null=True)),
                ('tonusmuscular', models.CharField(blank=True, max_length=30, null=True)),
                ('examenulcomplementarfield', models.TextField(blank=True, max_length=500, null=True)),
                ('diagnostic', models.TextField(blank=True, max_length=500, null=True)),
                ('tratament', models.TextField(blank=True, max_length=500, null=True)),
                ('animal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='animal.Animal')),
                ('consumabilefolosite', models.ManyToManyField(blank=True, null=True, through='fisa.ConsumabileFisa', to='inventariu.Consumabile')),
            ],
            options={
                'verbose_name_plural': 'Fise',
            },
        ),
        migrations.AddField(
            model_name='consumabilefisa',
            name='events',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fisa.Fisa'),
        ),
    ]
