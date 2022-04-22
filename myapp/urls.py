from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="home"),
    path('findflight', views.findflight, name="findflight"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('about/', views.about, name='about'),
    path('success', views.success, name="success"),
    path('payment', views.payment, name="payment"),
    path('complete', views.complete, name="complete"),
    # path('signout', views.signout, name="signout"),

]
