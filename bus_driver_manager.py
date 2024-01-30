from bus import Bus
from passenger import Passenger


class BusDriverManager:
    """A class representing a bus and its traffic management."""

    def __init__(self, drivers_name: str, drivers_bus: Bus):
        """
        Initialize a BusDriverManager object.

        Parameters:
        :param drivers_name (str): The name of the bus driver.
        :param drivers_bus (bus.Bus): The bus object associated with this driver.

        Upon initialization, the following attributes are set:
        - self.passengers (list): A list to store passengers associated with the bus driver.
        """
        self.driver = drivers_name
        self.drivers_bus = drivers_bus
        self.passenger_list = []

        drivers_bus.driver = self.driver
        drivers_bus.passengers = self.passenger_list

    def set_driver(self, driver: str):
        """Set a new bus driver."""
        self.driver = driver

    def get_passengers(self):
        """Get the list of passengers on the bus."""
        return self.passenger_list

    def get_seating_capacity(self):
        """Get the seating capacity of the bus."""
        return self.drivers_bus.seating_capacity

    def add_passengers(self, *args: Passenger):
        """Add one or more passengers to the bus."""
        passengers = [*args]
        for passenger in passengers:
            if len(self.passenger_list) < self.get_seating_capacity():
                if passenger.payment_status is True:
                    self.passenger_list.append(passenger)
                else:
                    print('The ticket is unpaid.')
            else:
                print('There are no free passenger seats on the bus.')

    def remove_passenger(self, passenger: Passenger):
        """Remove a passenger from the bus."""
        self.passenger_list.remove(passenger)

    def show_information(self):
        """Display information about the bus."""
        free_seats = self.get_seating_capacity() - len(self.passenger_list)
        print(f'Drivers name:                 {self.driver}\n'
              f'Drivers bus:                  {self.drivers_bus.registration_number}\n'
              f'Service name:                 {self.drivers_bus.service_name}\n'
              f'Passengers:                   {[passenger.passenger_name for passenger in self.passenger_list]}\n'
              f'Number of seats in the bus:   {self.get_seating_capacity()}\n'
              f'Number of passengers:         {len(self.passenger_list)}\n'
              f'The number of free seats:     {free_seats}\n')
