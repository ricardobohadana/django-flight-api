from django.db.models.query import QuerySet
from typing import Union, List

from ..models import Flight

class FlightEntity:
    

    # from api to db
    @staticmethod
    def is_a_valid_db_model(Model: dict):
        validity_set = {"flightNumber", "departureAirport", "arrivalAirport", 
                        "flightDate", "aircraft", "paxAvailable", "paxBooked"}

        return validity_set.issubset(Model.keys())

    @staticmethod    
    def is_a_valid_client_model(Model:dict):
        validity_set = {"flightNumber", "departureAirport", "arrivalAirport", 
                        "flightDate", "aircraft", "pax"}

        if validity_set.issubset(Model.keys()):
            sub_validity_set = {"available", "booked"}
            return sub_validity_set.issubset(Model["pax"].keys)

        return False


    @staticmethod
    def fromJsonToDbModel(data: dict) -> Flight:
        formatted_data = {key: data[key] for key in data.keys() if key != "pax"}
        formatted_data['paxAvailable'] = data["pax"]["available"]
        formatted_data['paxBooked'] = data["pax"]["booked"]
        
        return formatted_data

    # from db to api
    @staticmethod
    def fromQuerySetToJson(query_set: QuerySet, many=False) -> Union[List[dict], dict]:
        if many:
            data_list = list(query_set.values())
            formatted_data_list = []
            for data in data_list:
                formatted_data = {key: data[key] for key in data.keys() if key not in ['paxAvailable', 'paxBooked', '_state', 'created']}
                formatted_data["pax"] = {
                    "available": data['paxAvailable'],
                    "booked": data['paxBooked']
                }
                formatted_data_list.append(formatted_data)

            return formatted_data_list
        else:
            data = query_set.first().__dict__
            formatted_data = {key: data[key] for key in data.keys() if key not in ['paxAvailable', 'paxBooked', '_state', 'created']}
            formatted_data["pax"] = {
                "available": data['paxAvailable'],
                "booked": data['paxBooked']
            }
            
            return formatted_data