from twilio.rest import Client
import babel.numbers


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "ACbd68816dccbde2cdd3256211dcfa7722"
        self.auth_token = "f1ff9ee78b82c3b5b57891be2344fd25"
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, flight_details):
        price = babel.numbers.format_currency(number=flight_details['price'], currency="INR", locale="en_IN")
        from_city = f"{flight_details['origin_city']}-{flight_details['origin_airport']}"
        to_city = f"{flight_details['destination_city']}-{flight_details['destination_airport']}"
        departure_and_return = f"{flight_details['date_departure']} to {flight_details['date_return']}"

        message_body = f"Low price alert! Only {price} round trip to fly from {from_city} to {to_city}, from {departure_and_return}."
        if flight_details['via_city'] == "":
            message_body += f"\nFlight has {flight_details.stop_overs} stop over, via {flight_details.via_city}."

        message = self.client.messages \
            .create(
                body=message_body,
                from_='+18106443792',
                to='+917011576727'
        )
        return message
