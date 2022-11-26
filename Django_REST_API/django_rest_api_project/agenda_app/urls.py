from agenda_app.views import PrestadorList, AgendamentoDetails, AgendamentoList, get_horarios

from django.urls import path

urlpatterns = [
    
    path('prestadores/', PrestadorList.as_view()),
    path('agendamentos/', AgendamentoList.as_view()),
    path('agendamentos/<int:pk>', AgendamentoDetails.as_view()),
    path('horarios/', get_horarios)
]
