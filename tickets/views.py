from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


@login_required
def mis_tickets(request):
    tickets = Ticket.objects.filter(usuario=request.user)
    return render(request, 'mis_tickets.html', {'tickets': tickets})


@login_required
def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.usuario = request.user
            ticket.save()
            return redirect('mis_tickets')
    else:
        form = TicketForm()

    return render(request, 'crear_ticket.html', {'form': form})

@login_required
def detalle_ticket(request, id_ticket):
    ticket = get_object_or_404(Ticket, id=id_ticket, usuario=request.user)
    return render(request, 'detalle_ticket.html', {'ticket': ticket})
