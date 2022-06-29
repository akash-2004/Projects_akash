from flight_deals.data_manager import DataManager
from flight_deals.flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

data = data_manager.data
cities = data_manager.cities
city_prices = data_manager.prices
print(city_prices)
IATA_codes = flight_search.get_destination_codes(cities=cities)
data_manager.update_iatacodes(codes=IATA_codes)
flight_search.search_flights(codes=IATA_codes)
flight_search.compare_prices_send_sms(city_price=city_prices)
#MONTHY QUOTA REACHED by sheety problem, so gotta find an alternative
