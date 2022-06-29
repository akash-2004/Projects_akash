from flight_deals.flight_data import FlightData
from flight_deals.notification_manager import NotificationManager
import requests
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
LOCATION_SUFFIX = "/locations/query"
SEARCH_SUFFIX = "/v2/search"
AUTH_HEADER = {
    "accept": "application/json",
    "apikey": "jFrBELf_u5lMOf4l9vUjlxjVM-th79hP"
}

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_months_from_now = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")


class FlightSearch:
    def __init__(self):
        self.current_prices = {}

    def get_destination_codes(self, cities: list):
        """Returns a list of IATA codes of given cities."""
        codes = []
        for city in cities:
            parameter_locations = {
                "term": city,
                "location_types": "city",
                "locale": "en-US",
                "limit": 10,
                "active_only": True
            }
            response = \
                requests.get(url=f"{TEQUILA_ENDPOINT}{LOCATION_SUFFIX}", params=parameter_locations,
                             headers=AUTH_HEADER).json()["locations"][0]["code"]
            codes.append(response)
        return codes

    def search_flights(self, codes: list):
        """Finds current rates to the destination cities provided as their codes in a list.
         Returns a dictionary with city name and flight rate as key value pairs."""
        for code in codes:
            parameters = {
                "fly_from": "city:DEL",
                "fly_to": f"city:{code}",
                "date_from": tomorrow,
                "date_to": six_months_from_now,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "adults": 1,
                "max_stopovers": 0,
                "curr": "INR",
                "partner_market": "in"  # Use ISO 3166-1 alpha-2 to fill in the value
            }

            response = requests.get(url=f"{TEQUILA_ENDPOINT}{SEARCH_SUFFIX}", params=parameters,
                                    headers=AUTH_HEADER).json()

            try:
                data = response["data"][0]
            except IndexError:
                parameters["max_stopovers"] = 1
                response = requests.get(url=f"{TEQUILA_ENDPOINT}{SEARCH_SUFFIX}", params=parameters,
                                        headers=AUTH_HEADER).json()
                try:
                    data = response["data"][0]
                except IndexError:
                    continue  #Means no flights even with 1 stop over.
                else:
                    flight_data = FlightData(price=data["price"],
                                             origin_city=data["route"][0]["cityFrom"],
                                             origin_airport=data["route"][0]["flyFrom"],
                                             destination_city=data["route"][0]["cityTo"],
                                             destination_airport=data["route"][0]["flyTo"],
                                             date_departure=data["route"][0]["local_departure"].split("T")[0],
                                             date_return=data["route"][1]["local_departure"].split("T")[0],
                                             stop_overs=1,
                                             via_city=data["route"][0]["cityTo"]
                                             )
            else:
                flight_data = FlightData(price=data["price"],
                                         origin_city=data["route"][0]["cityFrom"],
                                         origin_airport=data["route"][0]["flyFrom"],
                                         destination_city=data["route"][0]["cityTo"],
                                         destination_airport=data["route"][0]["flyTo"],
                                         date_departure=data["route"][0]["local_departure"].split("T")[0],
                                         date_return=data["route"][1]["local_departure"].split("T")[0]
                                         )
            self.current_prices.update(flight_data.make_city_data_dict())

    def compare_prices_send_sms(self, city_price: dict):
        """"Compares current flight rates with lowest rates and sends sms if the new rate is lower."""
        notification_manager = NotificationManager()
        for city, price in city_price.items():
            try:
                if self.current_prices[city]["price"] < price:
                    # print(f"{city}\nOld price:{price} New price:{self.current_prices[city]}")
                    notification_manager.send_sms(self.current_prices[city])
            except KeyError:
                continue
