from django.shortcuts import render
from decimal import Decimal

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Flight, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


def home(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/base.html')
    else:
        return render(request, 'users/login.html')

def about(request):
    return render(request, 'myapp/about.html', {'title': 'About'})


@login_required(login_url='login')
def findflight(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')
        flight_list = Flight.objects.filter(source=source_r, dest=dest_r, date=date_r)
        if flight_list:
            return render(request, 'myapp/list.html', locals())
        else:
            context["error"] = "Sorry no flights available"
            return render(request, 'myapp/findflight.html', context)
    else:
        return render(request, 'myapp/findflight.html')


@login_required(login_url='login')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('flight_id')
        seats_r = int(request.POST.get('no_seats'))
        flight = Flight.objects.get(id=id_r)
        if flight:
            if flight.rem > int(seats_r):
                name_r = flight.flight_name
                cost = int(seats_r) * flight.price
                source_r = flight.source
                dest_r = flight.dest
                nos_r = Decimal(flight.nos)
                price_r = flight.price
                date_r = flight.date
                time_r = flight.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = flight.rem - seats_r
                Flight.objects.filter(id=id_r).update(rem=rem_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r, flight_name=name_r,
                                           source=source_r, flightid=id_r,
                                           dest=dest_r, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'myapp/bookings.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'myapp/findflight.html', context)

    else:
        return render(request, 'myapp/findflight.html')


@login_required(login_url='login')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('flight_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            flight = Flight.objects.get(id=book.flightid)
            rem_r = flight.rem + book.nos
            Flight.objects.filter(id=book.flightid).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(nos=0)
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that flight"
            return render(request, 'myapp/error.html', context)
    else:
        return render(request, 'myapp/findflight.html')


@login_required(login_url='login')
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'myapp/booklist.html', locals())
    else:
        context["error"] = "Sorry no flightes booked"
        return render(request, 'myapp/findflight.html', context)


@login_required(login_url='login')
def payment(request,new={}):
    return render(request, 'myapp/payment.html')


@login_required(login_url='login')
def complete(request,new={}):
    return render(request, 'myapp/complete.html')


def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'myapp/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'users/registers.html', context)
    else:
        return render(request, 'users/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'myapp/base.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'users/login.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'users/login.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'users/login.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'myapp/success.html', context)
