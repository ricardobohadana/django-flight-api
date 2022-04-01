from ..repositories.flight import FlightRepository
from ..entities.flight import FlightEntity

# Regras de Negócio
class FlightService:

    @staticmethod
    def get_flights_service():
        flights = FlightRepository.get_all()
        json_flight = FlightEntity.fromQuerySetToJson(flights, many=True)

        return json_flight

    @staticmethod
    def get_unique_flight_service(flight_id: str):
        flight = FlightRepository.get_unique(flight_id)
        json_flight = FlightEntity.fromQuerySetToJson(flight, many=False)
        return json_flight

    @staticmethod
    def post_flight_service(json_flight: dict):
        flight = FlightEntity.fromJsonToDbModel(json_flight)
        if FlightEntity.is_a_valid_db_model(flight):
            FlightRepository.save(flight)


    @staticmethod
    def book_cancel_flight_service(flight_id: str, available: int):
        operation = FlightRepository.update(flight_id, available)
        if operation:
            return True
        return False