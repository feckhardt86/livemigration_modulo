import uuid
from django.db import models


class TipoEvento(models.Model):
    descricao = models.CharField(max_length=45, null=True, blank=False)

    class Meta:
        verbose_name = 'Tipo de evento'
        verbose_name_plural = 'Tipos de evento'

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.descricao)


class ComputeNodes(models.Model):
    hypervisor_hostname = models.CharField(max_length=45, null=True, blank=False)


class Instances(models.Model):
    hostname = models.CharField(max_length=45, null=True, blank=False)
    uuid = models.CharField(max_length=45, null=True, blank=False)
    vcups = models.CharField(max_length=45, null=True, blank=False)
    memory_mb = models.CharField(max_length=45, null=True, blank=False)
    compute_nodes = models.ForeignKey(ComputeNodes, null=True,
                                      on_delete=models.SET_NULL,
                                      related_name='instances')

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.hostname)


class EventoEspecifico(models.Model):
    descricao = models.CharField(max_length=45, null=True, blank=False)
    percentual = models.IntegerField(null=True)
    frequencia = models.IntegerField(null=True)
    status = models.CharField(max_length=1, null=True, blank=False)
    tipo_evento = models.ForeignKey(TipoEvento, null=True, on_delete=models.SET_NULL)
    instances = models.ForeignKey(Instances, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.descricao)


class CadastroAutomatico(models.Model):
    descricao = models.CharField(max_length=45, null=True, blank=False)
    status = models.CharField(max_length=1, null=True, blank=False)
    historico = models.CharField(max_length=1, null=True, blank=False)
    cadastro_alarme = models.ForeignKey(EventoEspecifico, null=True,
                                        on_delete=models.SET_NULL)
    instances = models.ForeignKey(Instances, null=True,
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.descricao)


class EventoDinamico(models.Model):
    descricao = models.CharField(max_length=45, null=True, blank=False)
    status = models.CharField(max_length=1, null=True, blank=False)
    date = models.DateTimeField(null=True, blank=False)
    compute_node = models.ForeignKey(
        ComputeNodes, null=True, on_delete=models.SET_NULL, related_name='eventos_dinamicos')

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.descricao)


class CadastroAgendamento(models.Model):
    descricao = models.CharField(max_length=45, null=True, blank=False)
    data = models.DateTimeField(null=True)
    status = models.CharField(max_length=1, null=True, blank=False)
    instances = models.ForeignKey(Instances, null=True,
                                  on_delete=models.SET_NULL)
    compute_nodes = models.ForeignKey(ComputeNodes, null=True,
                                      on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.descricao)


class MovimentoManual(models.Model):
    descricao = models.CharField(max_length=45, null=True, blank=False)
    instances = models.ForeignKey(Instances, null=True,
                                  on_delete=models.SET_NULL)
    compute_nodes = models.ForeignKey(ComputeNodes, null=True,
                                      on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.descricao)


class MonitorEvento(models.Model):
    descricao = models.CharField(max_length=45, null=True, blank=False)
    descricao_evento = models.CharField(max_length=45, null=True, blank=False)
    status = models.CharField(max_length=45, null=True, blank=False)
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_fim = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.descricao)

