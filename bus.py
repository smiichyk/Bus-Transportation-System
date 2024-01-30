class Bus:
    """Represents the technical characteristics of a bus."""

    # variables used in the calc_dimensions function
    EXTRA_LARGE = 'Extra Large'
    LARGE = 'Large'
    AVERAGE = 'Average'
    SMALL = 'Small'
    PARTICULARLY_SMALL = 'Particularly Small'

    def __init__(self, registration_number: str, manufacturer: str, length: float, width: float, height: float,
                 seating_capacity: int, floors_number: int = 1, seat_belts: bool = False):
        """
        Initialize a Bus instance with technical characteristics.

        :param registration_number: (str) The registration number of the bus, a unique identifier.
        :param manufacturer: (str) The manufacturer of the bus.
        :param length: (float) The length of the bus in meters.
        :param width: (float) The width of the bus in meters.
        :param height: (float) The height of the bus in meters.
        :param seating_capacity: (int) The seating capacity of the bus.
        :param floors_number: (int) The number of floors in the bus (default = 1).
        :param seat_belts: (bool) Availability of seat belts for passengers (default is False).

        Upon initialization, the following attributes are set:
        - self.year: The manufacturing year of the bus, calculated from the registration number.
        - self.dimension: A calculated dimension attribute.

        Additional attributes are available for use when adding a bus to a BusService class:
        - self.service_name: The name of the bus service.
        - self.bus_route: The route or route number associated with the bus.
        - self.bus_station_list: A list of bus stations on the route.

        Additional attributes are available for use when adding a bus to a BusDriverManager class:
        - self.drivers_name: The name of the bus driver.
        - self.passengers: A list to store passenger information.
        """
        self.registration_number = registration_number
        self.manufacturer = manufacturer
        self.length = length
        self.width = width
        self.height = height
        self.seating_capacity = seating_capacity
        self.floors_number = floors_number
        self.seat_belts = seat_belts

        self.year = 2000 + int(registration_number[:2])
        self.dimension = self.calc_dimension()

        # attributes to use when adding a bus to a BusService class
        self.service_name = str
        self.bus_route = str
        self.bus_station_list = list

        # attributes to use when adding a bus to a BusDriverManager class
        self.drivers_name = str
        self.passengers = list

    def get_registration_number(self):
        """Get the registration number of the bus."""
        return self.registration_number

    def set_registration_number(self, registration_number: str):
        """Set the registration number of the bus."""
        self.registration_number = registration_number

    def calc_dimension(self):
        """Calculate the dimension category automatically based on seating capacity."""
        if self.seating_capacity >= 110:
            return Bus.EXTRA_LARGE
        elif self.seating_capacity >= 65:
            return Bus.LARGE
        elif self.seating_capacity >= 40:
            return Bus.AVERAGE
        elif self.seating_capacity >= 35:
            return Bus.SMALL
        elif self.seating_capacity > 0:
            return Bus.PARTICULARLY_SMALL

    def show_information(self):
        """Display all information about the bus."""
        print(f'Registration number:   {self.registration_number}\n'
              f'Manufacturer:          {self.manufacturer}\n'
              f'Year established:      {self.year}\n'
              f'Length:                {self.length}\n'
              f'Width:                 {self.width}\n'
              f'Height:                {self.height}\n'
              f'Seating capacity:      {self.seating_capacity}\n'
              f'Number of floors:      {self.floors_number}\n'
              f'Seat belts:            {self.seat_belts}\n'
              f'Dimensions:            {self.dimension}\n')


if __name__ == '__main__':
    aBus = Bus('22-D-34058', 'Wrightbus', 10.0, 2.52, 4.4,
               75, 2)
    aBus.show_information()
