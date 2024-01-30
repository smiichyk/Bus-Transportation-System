class Passenger:
    """Class representing a passenger and their payment status."""

    def __init__(self, passenger_name: str, payment_status: bool = False):
        """
        Initialize a Passenger object.

        :param passenger_name (str): The name of the passenger.
        :param payment_status (bool): The payment status (default is False).
        """
        self.passenger_name = passenger_name
        self.payment_status = payment_status

    def set_passenger_name(self, passenger_name: str):
        """Set a new name for the passenger."""
        self.passenger_name = passenger_name

    def set_payment_status(self, payment_status: bool):
        """Set a new payment status for the passenger."""
        self.payment_status = payment_status

    def show_information(self):
        """Display information about the passenger, including name and payment status."""
        print(f'Passenger name:    {self.passenger_name}\n'
              f'Payment status :   {self.payment_status}\n')


if __name__ == '__main__':
    aPassenger = Passenger('Nikita Smiichyk')
    aPassenger.show_information()
