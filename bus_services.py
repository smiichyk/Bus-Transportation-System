class BusServices:
    """A class to manage a collection of bus services."""

    def __init__(self, services_name: str):
        """
        Initialize a BusServices instance with a given name.

        :param services_name (str): The name of the bus services.

        Upon initialization, the following attributes are set:
        - self.bus_services (list): A list to store bus services associated with this instance.
        """
        self.services_name = services_name
        self.bus_service_list = []

    def set_services_name(self, services_name: str):
        """Set the name of the bus services."""
        self.services_name = services_name

    def set_bus_services(self, bus_services):
        """Set the list of BusService instances."""
        self.bus_service_list = bus_services

    def add_bus_service(self, service):
        """Add a BusService instance to the collection."""
        self.bus_service_list.append(service)

    def remove_bus_service(self, service):
        """Remove a BusService instance from the collection."""
        self.bus_service_list.remove(service)

    def show_information(self):
        """Display all information about the bus services."""
        bus_service_names = [service.service_name for service in self.bus_service_list]
        print(f'Bus services name:    {self.services_name}\n'
              f'Bus services:         {bus_service_names}\n'
              f'Bus services count:   {len(self.bus_service_list)}')


if __name__ == '__main__':
    aBusServices = BusServices('Navan Town Bus Services')
    aBusServices.show_information()
