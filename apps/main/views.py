from django.http import HttpResponse
from django.template import loader
from apps.main.models import *
from string import Template
from apps.main import utils
from django.contrib import messages
from django.shortcuts import redirect

from openstack import settings

LOCAL_FILE_FOLDER = '/media/' if settings.ON_HEROKU else '/etc/live/pend/'
ERROR_MESSAGE = 'Um erro ocorreu. Por favor tente mais tarde.'


def home(request):
    context = {}
    template = loader.get_template('main/home.html')
    return HttpResponse(template.render(context, request))


def monitor_eventos(request):
    context = {}
    logs = MonitorEvento.objects.all()
    context['logs'] = logs
    template = loader.get_template('main/monitor_eventos.html')
    return HttpResponse(template.render(context, request))


def migracao_manual(request):
    template = loader.get_template('main/migracao_manual.html')
    context = {}
    instances = Instances.objects.all()
    context['instances'] = instances
    c_nodes = ComputeNodes.objects.all()
    context['c_nodes'] = c_nodes

    if request.method == 'POST':
        try:
            desc = request.POST.get('descricao')
            instance = request.POST.get('instances')
            c_node = request.POST.get('compute_nodes')

            if desc and instance and c_node:
                mm = MovimentoManual.objects.create(
                    descricao=desc,
                    instances=Instances.objects.get(pk=instance),
                    compute_nodes=ComputeNodes.objects.get(pk=c_node)
                )
                mm.save()

                file_data = {
                    'descricao': mm.descricao,
                    'instancia': mm.instances.hostname,
                    'destino': mm.compute_nodes.hypervisor_hostname,
                    'uuid': mm.instances.uuid
                }
                file = open('apps/main/file_templates/manual_novo')
                src = Template(file.read())
                content = src.substitute(file_data)

                new_file_name = 'MANUAL_NOVO_' + str(mm.pk)
                new_file_src = LOCAL_FILE_FOLDER + new_file_name
                new_file = open(new_file_src, 'w+')
                new_file.write(content)
                new_file.close()

                messages.success(request, 'Realização de live migration, acompanhe o movimento de Eventos')
                #response = HttpResponse(content, content_type='text/plain')
                #response['Content-Disposition'] = \
                #    'attachment; filename="'+new_file_name+'"'
                #return response
        except Exception as e:
            messages.error(request, ERROR_MESSAGE)
            raise e

    return HttpResponse(template.render(context, request))


def migracao_especifico(request):
    template = loader.get_template('main/migracao_especifico.html')
    context = {}
    tipos = TipoEvento.objects.all()
    context['tipos'] = tipos
    instances = Instances.objects.all()
    context['instances'] = instances

    if request.method == 'POST':
        try:
            descricao = request.POST.get('descricao')
            percentual = request.POST.get('percentual')
            frequencia = request.POST.get('frequencia')
            tipo_evento = request.POST.get('tipo_evento')
            instance = request.POST.get('instances')

            evento = EventoEspecifico.objects.create(
                descricao=descricao,
                percentual=percentual,
                frequencia=frequencia,
                status='1',
                tipo_evento=TipoEvento.objects.get(pk=tipo_evento),
                instances=Instances.objects.get(pk=instance),
            )
            evento.save()

            file_data = {
                'evento_descricao': evento.descricao,
                'tipo_evento': evento.tipo_evento.descricao,
                'evento_percentual': evento.percentual,
                'evento_frequencia': evento.frequencia,
                'instancia': evento.instances.hostname,
                'uuid': evento.instances.uuid
            }
            file = open('apps/main/file_templates/especifico_novo')
            src = Template(file.read())
            content = src.substitute(file_data)

            new_file_name = 'ESPECIFICO_NOVO_' + str(evento.pk)
            new_file_src = LOCAL_FILE_FOLDER + new_file_name
            new_file = open(new_file_src, 'w+')
            new_file.write(content)
            new_file.close()

            messages.success(request, 'Realização de live migration, acompanhe o movimento de Eventos')
            #response = HttpResponse(content, content_type='text/plain')
            #response['Content-Disposition'] = \
            #    'attachment; filename="' + new_file_name + '"'
            #return response

        except Exception as e:
            messages.error(request, ERROR_MESSAGE)
            raise e

    return HttpResponse(template.render(context, request))


def migracao_dinamico(request):
    template = loader.get_template('main/migracao_dinamico.html')
    context = {}

    if request.method == 'POST':
        try:
            descricao = request.POST.get('descricao')
            data = utils.format_date(request.POST.get('data'))

            evento = EventoDinamico.objects.create(
                descricao=descricao,
                status='1',
                date=data,
            )
            evento.save()

            file_data = {
                'descricao': evento.descricao,
                'data': evento.date,
            }
            file = open('apps/main/file_templates/dinamico_novo')
            src = Template(file.read())
            content = src.substitute(file_data)

            new_file_name = 'DINAMICO_NOVO_' + str(evento.pk)

            new_file_src = LOCAL_FILE_FOLDER + new_file_name
            new_file = open(new_file_src, 'w+')
            new_file.write(content)
            new_file.close()

            messages.success(request, 'Cadastro de Dinamico de live migration criado com sucesso')

            #response = HttpResponse(content, content_type='text/plain')
            #response['Content-Disposition'] = \
            #    'attachment; filename="' + new_file_name + '"'
            #return response
        except Exception as e:
            messages.error(request, ERROR_MESSAGE)
            raise e

    return HttpResponse(template.render(context, request))


# def automatico_live_migration(request):
#     template = loader.get_template('main/automatico_live_migration.html')
#     context = {}
#     alarmes = EventoEspecifico.objects.filter(status='1')
#     context['alarmes'] = alarmes
#     instances = Instances.objects.all()
#     context['instances'] = instances
#
#     if request.method == 'POST':
#         try:
#             descricao = request.POST.get('descricao')
#             historico = request.POST.get('historico')
#             cadastro_alarme = request.POST.get('cadastro_alarme')
#             instances = request.POST.get('instances')
#
#             ca = CadastroAutomatico.objects.create(
#                 descricao=descricao,
#                 status='1',
#                 historico=historico,
#                 cadastro_alarme=EventoEspecifico.objects.get(pk=cadastro_alarme),
#                 instances=Instances.objects.get(pk=instances)
#             )
#             ca.save()
#
#             file_data = {
#                 'descricao': ca.descricao,
#                 'instancia': ca.instances.hostname,
#                 'parametro': ca.historico,
#                 'evento_descricao': ca.cadastro_alarme.descricao,
#                 'evento_percentual': ca.cadastro_alarme.percentual,
#                 'evento_frequencia': ca.cadastro_alarme.frequencia
#             }
#             file = open('apps/main/file_templates/especifico_novo')
#             src = Template(file.read())
#             content = src.substitute(file_data)
#
#             new_file_name = 'AUTOMATICO_NOVO_' + str(ca.pk)
#
#             new_file_src = LOCAL_FILE_FOLDER + new_file_name
#             new_file = open(new_file_src, 'w+')
#             new_file.write(content)
#             new_file.close()
#
#             messages.success(request, 'Cadastro Automático de live migration criado com sucesso')
#
#             response = HttpResponse(content, content_type='text/plain')
#             response['Content-Disposition'] = \
#                 'attachment; filename="' + new_file_name + '"'
#             return response
#         except Exception:
#             messages.error(request, ERROR_MESSAGE)
#
#     return HttpResponse(template.render(context, request))


def listagem(request):
    template = loader.get_template('main/listagem.html')
    context = {
        'eventos_especificos': EventoEspecifico.objects.filter(status='1'),
        'eventos_dinamicos': EventoDinamico.objects.filter(status='1'),
    }
    return HttpResponse(template.render(context, request))


def del_especifico(request, pk=None):
    if pk:
        # Altera status para '0'
        evento = EventoEspecifico.objects.get(pk=pk)
        evento.status = '0'
        evento.save()
        new_file_name = 'DINAMICO_DELETE_' + str(evento.pk)
        new_file_src = LOCAL_FILE_FOLDER + new_file_name
        new_file = open(new_file_src, 'w+')
        new_file.close()
        messages.success(request, 'Evento excluido com sucesso')
    return redirect('url_listagem')


def del_dinamico(request, pk=None):
    if pk:
        # Altera status para '0'
        evento = EventoDinamico.objects.get(pk=pk)
        evento.status = '0'
        evento.save()
        new_file_name = 'ESPECIFICO_DELETE_' + str(evento.pk)
        new_file_src = LOCAL_FILE_FOLDER + new_file_name
        new_file = open(new_file_src, 'w+')
        new_file.close()
        messages.success(request, 'Evento excluido com sucesso')
    return redirect('url_listagem')


def relatorio_eventos(request):
    template = loader.get_template('main/relatorio_eventos.html')
    context = {
        'eventos_especificos': EventoEspecifico.objects.filter(status='1'),
        'eventos_dinamicos': EventoDinamico.objects.filter(status='1'),
    }
    return HttpResponse(template.render(context, request))


# def listagem_auto_migrations(request, pk=None):
#     template = loader.get_template('main/listagem_auto_migrations.html')
#     context = {}
#
#     if pk:
#         # 'Exclui' o alarme (Altera status para '0')
#         ca = CadastroAutomatico.objects.get(pk=pk)
#         ca.status = '0'
#         ca.save()
#
#         # Refresh lista de cadastros
#         cadastros = CadastroAutomatico.objects.filter(status='1')
#         context['cadastros'] = cadastros
#
#         new_file_name = 'AUTOMATICO_DELETE_' + str(ca.pk)
#
#         new_file_src = LOCAL_FILE_FOLDER + new_file_name
#         new_file = open(new_file_src, 'w+')
#         new_file.close()
#
#         messages.success(request, 'Item excluído com sucesso')
#
#         response = HttpResponse('', content_type='text/plain')
#         response['Content-Disposition'] = \
#             'attachment; filename="' + new_file_name + '"'
#         return response
#     else:
#         cadastros = CadastroAutomatico.objects.filter(status='1')
#         context['cadastros'] = cadastros
#         return HttpResponse(template.render(context, request))


# def listagem_agendamento_migrations(request, pk=None):
#     template = loader.get_template('main/listagem_agendamento_migrations.html')
#     context = {}
#
#     if pk:
#         # 'Exclui' o alarme (Altera status para '0')
#         ca = CadastroAgendamento.objects.get(pk=pk)
#         ca.status = '0'
#         ca.save()
#
#         # Refresh lista de cadastros
#         cadastros = CadastroAgendamento.objects.filter(status='1')
#         context['cadastros'] = cadastros
#
#         new_file_name = 'AGENDAMENTO_DELETE_' + str(ca.pk)
#
#         new_file_src = LOCAL_FILE_FOLDER + new_file_name
#         new_file = open(new_file_src, 'w+')
#         new_file.close()
#
#         messages.success(request, 'Item excluído com sucesso')
#
#         response = HttpResponse('', content_type='text/plain')
#         response['Content-Disposition'] = \
#             'attachment; filename="' + new_file_name + '"'
#         return response
#     else:
#         cadastros = CadastroAgendamento.objects.filter(status='1')
#         context['cadastros'] = cadastros
#         return HttpResponse(template.render(context, request))
