from agenda_app.views import PrestadorList, AgendamentoDetails, AgendamentoList

from django.urls import path

urlpatterns = [
    path('prestadores/', PrestadorList.as_view()),
    path('agendamentos/', AgendamentoList.as_view()),
    path('agendamentos/<int:pk>', AgendamentoDetails.as_view()),
]
