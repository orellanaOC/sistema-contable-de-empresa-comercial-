# Generated by Django 2.2.5 on 2019-11-24 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='valorInicial',
            fields=[
                ('idValor', models.AutoField(primary_key=True, serialize=False)),
                ('fechaInicio', models.DateField()),
                ('fechaFinal', models.DateField()),
                ('saldo', models.FloatField(null=True)),
                ('estadoCuenta', models.CharField(choices=[('A', 'ACREEEDORA'), ('D', 'DEUDORA'), ('S', 'SALDADA'), ('P', 'PATRIMONIO')], default='S', max_length=1)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuenta.Cuenta')),
            ],
        ),
    ]
