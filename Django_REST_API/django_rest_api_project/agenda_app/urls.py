from views import agendamento_details

from django.urls import path

urlpatterns = [
    path('agendamentos/<int:id>', agendamento_details),
]
