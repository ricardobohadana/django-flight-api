from enum import unique
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..services.flight import FlightService


class FlightController:

    @staticmethod
    def get_flights(request: Request) -> Response:
        json_flights = FlightService.get_flights_service()
        return Response(json_flights, status=status.HTTP_200_OK)

    @staticmethod
    def get_unique_flight(request: Request) -> Response:
        try:
            flight_id = request.query_params['flight']
            json_flight = FlightService.get_unique_flight_service(flight_id)
        except KeyError:
            return Response({"erro": "Não foi recebido o parâmetro flight, responsável por selecionar um vôo específico para retornar"}, status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response({"erro": "Não foi encontrado um vôo no banco de dados com o parâmetro especificado."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(json_flight, status=status.HTTP_200_OK)
        
        
    @staticmethod
    def post_flight(request: Request) -> Response:
        if not request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        json_flight = request.data
        FlightService.post_flight_service(json_flight)
        return Response(status=status.HTTP_201_CREATED)
        
    @staticmethod
    def book_flight(request: Request, flight: str) -> Response:
        try:
            flight_id = flight
            success = FlightService.book_cancel_flight_service(flight_id, -1)
            if success:
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except AttributeError:
            return Response({"erro": "Não foi encontrado um vôo no banco de dados com o parâmetro especificado."}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def cancel_book(request: Request, flight: str) -> Response:
        try:
            flight_id = flight
            success = FlightService.book_cancel_flight_service(flight_id, 1)
            if success:
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except AttributeError:
            return Response({"erro": "Não foi encontrado um vôo no banco de dados com o parâmetro especificado."}, status=status.HTTP_400_BAD_REQUEST)