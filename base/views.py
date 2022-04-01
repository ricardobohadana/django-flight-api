from os import stat
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from .controllers.flight import FlightController

@api_view(['GET', 'POST'])
def flight(request: Request):
    '''
    get:
    Retorna um único objeto.

    Endpoint utilizado para retornar um único objeto Flight de acordo com o parâmetro /?flight=flight_id

    post:
    Utilizado para criar um novo objeto.

    Endpoint utilizado para cadastrar, no banco de dados, um único objeto Flight de acordo com os dados enviados.
    '''
    if request.method == 'GET':            
        return FlightController.get_unique_flight(request)
    elif request.method == 'POST':
        return FlightController.post_flight(request)

@api_view(['GET'])
def getFlights(request: Request):
    '''
    get:
    Retorna uma lista com todos os objetos do banco de dados.

    Endpoint utilizada para retornar todos os objetos 'Flight' do banco de dados.
    '''
    return FlightController.get_flights(request)

@api_view(['PUT'])
def bookFlight(request: Request, flight: str):
    '''
    put:
    Utilizada para realizar uma reserva em um único objeto de vôo.

    Endpoint utilizada para confirmar uma reserva em um único objeto 'Flight' do banco de dados, identificado com o parâmetro {flight} enviado pela requisição.
    '''
    if not flight:
        return Response({"erro": "Não foi recebido o parâmetro flight, responsável por selecionar um voo específico para realizar sua reserva"}, status=status.HTTP_400_BAD_REQUEST)

    return FlightController.book_flight(request, flight)



@api_view(['PUT'])
def cancelBook(request: Request, flight: str):
    '''
    put:
    Utilizada para cancelar uma reserva em um único objeto de vôo.

    Endpoint utilizada para cancelar uma reserva em um único objeto 'Flight' do banco de dados, identificado com o parâmetro {flight} enviado pela requisição.
    '''
    if not flight:
        return Response({"erro": "Não foi recebido o parâmetro 'flight', responsável por selecionar um voo específico para cancelar sua reserva"}, status=status.HTTP_400_BAD_REQUEST)
    return FlightController.cancel_book(request, flight)