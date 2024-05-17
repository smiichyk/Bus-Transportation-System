 # Bus Management System

## Overview
This project is a comprehensive bus management system designed to handle various aspects of bus operations, including technical specifications, driver management, passenger handling, and service routes. The system comprises several interconnected classes, each responsible for specific functionalities.

## Features
- **Bus Class**: Represents the technical characteristics of a bus.
- **BusDriverManager Class**: Manages bus drivers and passengers.
- **BusService Class**: Manages bus routes and stations.
- **BusServices Class**: Manages multiple bus services.
- **Passenger Class**: Represents a passenger with a name and payment status.

## Classes and Methods

### Bus Class
Represents the technical characteristics of a bus.

#### Attributes:
- **registration_number (str)**: The registration number of the bus.
- **manufacturer (str)**: The manufacturer of the bus.
- **length (float)**: The length of the bus in meters.
- **width (float)**: The width of the bus in meters.
- **height (float)**: The height of the bus in meters.
- **seating_capacity (int)**: The seating capacity of the bus.
- **floors_number (int)**: The number of floors in the bus.
- **seat_belts (bool)**: Availability of seat belts for passengers.
- **year (int)**: The manufacturing year of the bus, derived from the registration number.
- **dimension (str)**: Dimension category based on seating capacity.
- Additional attributes for service and driver management.

#### Methods:
- `get_registration_number()`: Returns the registration number.
- `set_registration_number(registration_number: str)`: Sets the registration number.
- `calc_dimension()`: Calculates the dimension category based on seating capacity.
- `show_information()`: Displays all information about the bus.

### BusDriverManager Class
Manages bus drivers and their associated buses and passengers.

#### Attributes:
- **driver (str)**: The name of the bus driver.
- **drivers_bus (Bus)**: The bus associated with this driver.
- **passenger_list (list)**: List of passengers on the bus.

#### Methods:
- `set_driver(driver: str)`: Sets a new bus driver.
- `get_passengers()`: Returns the list of passengers.
- `get_seating_capacity()`: Returns the seating capacity of the bus.
- `add_passengers(*args: Passenger)`: Adds one or more passengers to the bus.
- `remove_passenger(passenger: Passenger)`: Removes a passenger from the bus.
- `show_information()`: Displays information about the bus and its passengers.

### BusService Class
Manages a bus service, including its name, route, and associated buses and stations.

#### Attributes:
- **service_name (str)**: The name of the bus service.
- **bus_route (str)**: The route followed by the bus.
- **bus_station_list (list)**: List of bus stations on the route.
- **bus_list (list)**: List of buses associated with this service.

#### Methods:
- `set_service_name(service_name: str)`: Sets the name of the bus service.
- `set_bus_route(bus_route: str)`: Sets the bus route.
- `set_bus_station_list(bus_station_list: list)`: Sets the list of bus stations.
- `add_bus_station(bus_station: str, index=None)`: Adds a bus station to the route.
- `remove_bus_station(bus_station=None, index=None)`: Removes a bus station from the route.
- `get_bus_by_registration_number(registration_number: str)`: Returns a bus by its registration number.
- `add_bus(bus: Bus)`: Adds a bus to the service.
- `remove_bus(bus: Bus)`: Removes a bus from the service.
- `show_information()`: Displays all information about the bus service.

### BusServices Class
Manages a collection of bus services.

#### Attributes:
- **services_name (str)**: The name of the bus services.
- **bus_service_list (list)**: List of bus services.
