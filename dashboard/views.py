from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ReserveForm


# Create your views here.



@login_required
def dashboard(request):
    reservation = Reservation.objects.all()
    customer = Customer.objects.all()

    total_customer = customer.count()
    total_reservation = reservation.count()

    ended = reservation.filter(status='Ended').count()
    pending = reservation.filter(status='Pending').count()

    context = {'reservation': reservation, 'customer': customer, 'total_reservation': total_reservation, 'ended': ended, 'pending': pending}

    return render(request, 'dashboard/dashboard.html', context)


def carsList(request):
    car = Car.objects.all()
    return render(request, 'dashboard/carsList.html', {'car': car})


def customers(request, pk):

    customer = Customer.objects.get(id=pk)

    reservation = customer.reservation_set.all()
    reservation_count = reservation.count()

    context = {'customer': customer, 'reservation': reservation, 'reservation_count': reservation_count}
    return render(request, 'dashboard/customers.html', context)


def createReservation(request, pk):
    customer = Customer.objects.get(id=pk)
    form = ReserveForm()
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'dashboard/reservation_form.html', context)


def updateReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    form = ReserveForm(instance=reservation)

    if request.method == 'POST':
        form = ReserveForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'dashboard/reservation_form.html', context)


def deleteReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == "POST":
        reservation.delete()
        return redirect('/')
    context = {'item': reservation}
    return render(request, 'dashboard/delete.html', context)
