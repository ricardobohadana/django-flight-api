# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .repositories.flight import FlightRepository
# from django.test import TransactionTestCase

# # testing endpoint /flight
# class GetFlight(APITestCase, TransactionTestCase):

#     def test_handle_missing_query_param(self):
#         """
#         Ensure there is a proper error handling if not receiving correct 
#         query parameter in /flight
#         """

#         url = reverse('flight')
#         data = {}
#         response = self.client.get(url, data)
        
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_handle_flight_not_found(self):
#         """
#         Ensure there is a proper error handling if no flight is found 
#         matchin query parameter
#         """

#         url = reverse('flight')
#         data = {}
#         response = self.client.get(url, data)
        
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_returns_correct_data(self):

#         print(FlightRepository.get_all())
#         # print('-------------------')
#         # response = self.client.get("/flight?flight=BAL1234")
#         # response_data = {
#         #     "flightNumber": "BAL1234",
#         #     "departureAirport": "SBGR",
#         #     "arrivalAirport": "SBGL",
#         #     "flightDate": 1648514594,
#         #     "aircraft": "A32N",
#         #     "pax": {
#         #         "available": 152,
#         #         "booked": 103
#         #     }
#         # }
#         # print(response)
#         # print(response.json())
#         # self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # self.assertDictEqual(response_data, response.data)

        
        

