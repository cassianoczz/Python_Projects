from agenda_app.views import AgendamentoDetails, AgendamentoList

from django.urls import path

urlpatterns = [
    path('agendamentos/', AgendamentoList.as_view()),
    path('agendamentos/<int:pk>', AgendamentoDetails.as_view()),
]
