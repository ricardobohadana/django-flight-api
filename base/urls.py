from django.urls import path
from . import views

urlpatterns = [
    path('flight', views.flight, name='flight'),
    path('flights/', views.getFlights, name='flights'),
    path('book/<str:flight>', views.bookFlight, name='book-flight'),
    path('cancel/<str:flight>', views.cancelBook, name='cancel-book')
]