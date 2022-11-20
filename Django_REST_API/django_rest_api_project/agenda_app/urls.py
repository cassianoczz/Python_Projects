from agenda_app.views import agendamento_details, agendamento_list

from django.urls import path

urlpatterns = [
    path('agendamentos/', agendamento_list),
    path('agendamentos/<int:id>', agendamento_details),
]
