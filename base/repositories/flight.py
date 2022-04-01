from xml.dom.minidom import Attr
from ..models import Flight
from django.db.models import QuerySet
from ..entities.flight import FlightEntity


class FlightRepository:

    @staticmethod
    def update(flight: str, available: int) -> bool:
        flight_queryset = FlightRepository.get_unique(flight)
        try:
            flight_dict = flight_queryset.first().__dict__
        except AttributeError:
            raise AttributeError
        newAvailable = flight_dict["paxAvailable"] + available
        newBooked = flight_dict["paxBooked"] - available
        flight_queryset.update(paxAvailable=newAvailable, paxBooked=newBooked)
        return True


    @staticmethod
    def save(flight_data) -> bool:
        if FlightEntity.is_a_valid_db_model(flight_data):
            Flight.objects.create(**flight_data)

            return True
        return False
    
    @staticmethod
    def get_all() -> QuerySet:
        flights = Flight.objects.all()
        return flights


    @staticmethod
    def get_unique(flight: str) -> QuerySet:
        flights = Flight.objects.filter(flightNumber=flight)
        return flights

