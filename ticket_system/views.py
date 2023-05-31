from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ticket, comment, customer
from .forms import TicketForm, CommentForm, CustomerForm
from django.core.paginator import Paginator



# Create your views here.

def tickets_list_view(request):
    if request.user.is_authenticated:
        tickets = ticket.objects.all()
        p = Paginator(tickets, 10)
        page = request.GET.get('page')
        p_tickets = p.get_page(page)

        return render(request, "tickets/ticket_list.html", {'p_tickets':p_tickets})
    else:
        return redirect('users:login')
    
def ticket_detail_view(request, pk):
    ticket_detail = ticket.objects.get(id=pk)
    comments = comment.objects.filter(ticket=ticket_detail)
    context = {
        'ticket': ticket_detail,
        'comments': comments,
    }
    return render(request, "tickets/ticket_detail.html", context)

def create_ticket_view(request):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ticket_list')
         
    return render(request, "tickets/create_ticket.html", {'form':form})

def update_ticket_list(request, pk):
    tickets = ticket.objects.get(id=pk)
    form = TicketForm(instance = tickets)
    if request.method == 'POST':
        form =TicketForm(request.POST, instance =tickets)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')


    return render(request, "tickets/create_ticket.html", {'form':form})

def delete_ticket_list(request, pk):
    get_ticket = ticket.objects.get(id=pk)
    if request.method =='POST':
        get_ticket.delete()
        return redirect('ticket_list')

    return render(request, "tickets/delete_ticket.html", {'ticket':get_ticket})

def add_ticket_comment(request, pk):
    get_ticket = ticket.objects.get(id=pk)
    form= CommentForm(ticket=get_ticket, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.ticket = get_ticket
            new_comment.save()
            return redirect('ticket_list')

    context = {
        'ticket': get_ticket,
        'form':form,
    }

    return render(request, "tickets/add_ticket_comment.html", context)

def add_customer_list(request):
    form = CustomerForm()
    if request.method =='POST':
        form = CustomerForm(request.POST or None)
        if form.is_valid:
            first_name = request.POST['first_name']
            last_name  = request.POST['last_name']

            if not customer.objects.filter(first_name=first_name, last_name=last_name).exists():
                form.save()
                return redirect('ticket_list')
            else:
                messages.info(request, ("Customer First Name and Last name already exist!"))
                return redirect('customer_add')
    context ={
        'form':form
    }

    return render(request, "tickets/add_customer_list.html", context)

def customer_list_view(request):
    customers = customer.objects.all()
    p = Paginator(customers, 10)
    page = request.GET.get('page')
    p_customers = p.get_page(page)

    return render(request, "tickets/customer_ticket_list.html", {'p_customers':p_customers})