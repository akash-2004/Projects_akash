import requests

SHEETY_ENDPOINT1 = "https://api.sheety.co/a80d0a3e660aaa462a84c5eaf79e25f1/flightPrices/prices"
SHEETY_ENDPOINT = "https://api.sheety.co/6bf3ac8ebc572a56eb9ff8f267e1a25c/flightPrices/prices"
AUTH_SHEETY = {
    "Authorization": "Bearer rosslovesdinosaurs",
    "Content-Type": "application/json"
}


class DataManager:

    def __init__(self):
        self.data = {}
        self.cities = []
        self.prices = {}
        self.get_cities()
        self.get_prices()

    def get_db(self):
        """Gets the data from the spreadsheet."""
        self.data = requests.get(url=SHEETY_ENDPOINT, headers=AUTH_SHEETY)
        self.data.raise_for_status()
        self.data = self.data.json()["prices"]
        return self.data

    def get_cities(self):
        """Returns list of cities."""
        self.data = self.get_db()
        self.cities = [i["city"] for i in self.data]

        return self.cities

    def update_iatacodes(self, codes: list):
        """Updates IATA codes in the database."""
        row_id = 1
        for code in codes:
            row_id += 1
            input_data = {
                "price": {
                    "iataCode": code
                }
            }
            put_data = requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", json=input_data, headers=AUTH_SHEETY)
            put_data.raise_for_status()

    def get_prices(self):
        "Returns a dictionary with city name and lowest price as key value pairs from the database."
        self.prices = {i["city"]: i["lowestPrice"] for i in self.data}
        return self.prices
