class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city,
                 destination_airport, date_departure, date_return, stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.date_departure = date_departure
        self.date_return = date_return
        self.stop_overs = stop_overs
        self.via_city = via_city
        self.data = (self.price, self.origin_city, self.origin_airport, self.destination_city, self.destination_airport,
                     self.date_departure, self.date_return)

    def make_city_data_dict(self):
        city_dict = {self.destination_city: {"price": self.price,
                                             "origin_city": self.origin_city,
                                             "origin_airport": self.origin_airport,
                                             "destination_city":self.destination_city,
                                             "destination_airport": self.destination_airport,
                                             "date_departure": self.date_departure,
                                             "date_return": self.date_return,
                                             "stop_overs": self.stop_overs,
                                             "via_city": self.via_city
                                             }}
        return city_dict
