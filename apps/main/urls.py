from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Menu Monitor
    path('monitor-eventos', views.monitor_eventos, name='url_monitor_eventos'),

    # Menu Evento
    path('migracao-manual', views.migracao_manual, name='url_migracao_manual'),
    path('migracao-especifico', views.migracao_especifico, name='url_migracao_especifico'),
    path('migracao-evento-dinamico', views.migracao_dinamico, name='url_migracao_evento_dinamico'),

    # Menu Listagem
    path('listagem/', views.listagem, name='url_listagem'),
    path('listagem/del_especifico/<int:pk>', views.del_especifico, name='url_del_especifico'),
    path('listagem/del_dinamico/<int:pk>', views.del_dinamico, name='url_del_dinamico'),

    # Menu Relatório
    path('relatorio_eventos/', views.relatorio_eventos, name='url_eventos'),

]
