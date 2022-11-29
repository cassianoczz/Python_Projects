from agenda_app.views import relatorio_prestador, AgendamentoDetails, AgendamentoList, get_horarios, healthcheck

from django.urls import path

urlpatterns = [
    
    path('prestadores/', relatorio_prestador),
    path('agendamentos/', AgendamentoList.as_view()),
    path('agendamentos/<int:pk>', AgendamentoDetails.as_view()),
    path('horarios/', get_horarios),
    path('', healthcheck)
]
