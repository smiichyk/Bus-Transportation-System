from bus import Bus


class BusService:
    """Represents a bus service with a name and a route, and can manage bus stations and buses."""

    def __init__(self, service_name: str, bus_route: str):
        """
        Initialize a BusService instance with a service name and a bus route.

        :param service_name (str): The name of the bus service.
        :param bus_route (str): The start and end of the route followed by the bus.

        Upon initialization, the following attributes are set:
        - self.bus_station_list (list): A list to store bus stations along the route.
        - self.bus_list (list): A list to store buses associated with this service.
        """
        self.service_name = service_name
        self.bus_route = bus_route
        self.bus_station_list = []
        self.bus_list = []

    def set_service_name(self, service_name: str):
        """Set the name of the bus service."""
        self.service_name = service_name

    def set_bus_route(self, bus_route: str):
        """Set the bus route of the service."""
        self.bus_route = bus_route

    def set_bus_station_list(self, bus_station_list: list):
        """Set the list of bus stations on the route."""
        self.bus_station_list = bus_station_list

    def add_bus_station(self, bus_station: str, index=None):
        """Add a bus station to the list of stations on the route, optionally specifying its position."""
        if index is not None:
            self.bus_station_list.insert(index, bus_station)
        else:
            self.bus_station_list.append(bus_station)

    def remove_bus_station(self, bus_station=None, index=None):
        """Remove a bus station from the list of stations on the route, optionally specifying its name or position."""
        if bus_station in self.bus_station_list:
            if index is None:
                self.bus_station_list.remove(bus_station)
        else:
            if index is not None:
                self.bus_station_list.pop(index - 1)
            else:
                print('The name of the bus station is entered incorrectly, or this station is not in the list.')

    def get_bus_by_registration_number(self, registration_number: str):
        """Get a bus from the list by its registration number."""
        for bus in self.bus_list:
            if bus.registration_number == registration_number:
                return bus

    def add_bus(self, bus: Bus):
        """Add a Bus instance to the collection."""
        bus.service_name = self.service_name
        bus.bus_route = self.bus_route
        bus.bus_station_list = self.bus_station_list
        self.bus_list.append(bus)

    def remove_bus(self, bus):
        """Remove a Bus instance from the collection."""
        if bus in self.bus_list:
            self.bus_list.remove(bus)
        else:
            print('The bus is not in the list.')

    def show_information(self):
        """Display all information about the bus service."""
        print(f'Service name:    {self.service_name}\n'
              f'Bus route:       {self.bus_route}\n'
              f'Bus stations:    {self.bus_station_list}\n'
              f'Buses:           {[b.registration_number for b in self.bus_list]}\n')


if __name__ == '__main__':
    aBusService = BusService('101', 'Drogheda-Dublin')
    aBusService.show_information()
