from django.urls import path
from .views import tickets_list_view, create_ticket_view, ticket_detail_view

app_name = 'tickets'

urlpatterns = [
     path('TicketList/', tickets_list_view, name='ticket_list'),
     path('createTicket', create_ticket_view, name='ticket_create'),
     path('<int:pk>/', ticket_detail_view, name='ticket_detail'),
     
]    