# Generated by Django 2.1.2 on 2018-10-21 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroAgendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45, null=True)),
                ('data', models.DateField(null=True)),
                ('status', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CadastroAlarme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45, null=True)),
                ('percentual', models.IntegerField(null=True)),
                ('frequencia', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CadastroAutomatico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45, null=True)),
                ('status', models.CharField(max_length=1, null=True)),
                ('historico', models.CharField(max_length=1, null=True)),
                ('cadastro_alarme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.CadastroAlarme')),
            ],
        ),
        migrations.CreateModel(
            name='ComputeNodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hypervisor_hostname', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=45, null=True)),
                ('uuid', models.CharField(max_length=45, null=True)),
                ('vcups', models.CharField(max_length=45, null=True)),
                ('memory_mb', models.CharField(max_length=45, null=True)),
                ('compute_nodes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instances', to='main.ComputeNodes')),
            ],
        ),
        migrations.CreateModel(
            name='LogsLiveMotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45, null=True)),
                ('descricao_evento', models.CharField(max_length=45, null=True)),
                ('status', models.CharField(max_length=45, null=True)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovimentoManual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45, null=True)),
                ('compute_nodes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.ComputeNodes')),
                ('instances', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Instances')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'Tipo de evento',
                'verbose_name_plural': 'Tipos de evento',
            },
        ),
        migrations.AddField(
            model_name='cadastroautomatico',
            name='instances',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Instances'),
        ),
        migrations.AddField(
            model_name='cadastroalarme',
            name='tipo_evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.TipoEvento'),
        ),
        migrations.AddField(
            model_name='cadastroagendamento',
            name='compute_nodes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.ComputeNodes'),
        ),
        migrations.AddField(
            model_name='cadastroagendamento',
            name='instances',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Instances'),
        ),
    ]
