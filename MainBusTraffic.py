from bus import Bus
from passenger import Passenger
from bus_service import BusService
from bus_driver_manager import BusDriverManager
from bus_services import BusServices


def bus_34058():
    """Create a Bus object for bus with registration number '22-D-34058'."""
    bus = Bus('22-D-34058', 'Wrightbus', 10.0, 2.52, 4.4,
              75, 2)
    return bus


def bus_41353():
    """Create a Bus object for bus with registration number '20-D-41353'."""
    bus = Bus('20-D-41353', 'Wrightbus', 12.0, 2.52, 2.8,
              63, seat_belts=True)
    return bus


def bus_43060():
    """Create a Bus object for bus with registration number '21-D-43060'."""
    bus = Bus('21-D-43060', 'Wrightbus', 10.0, 2.52, 4.4,
              75, 2)
    return bus


def bus_40323():
    """Create a Bus object for bus with registration number '23-D-40323'."""
    bus = Bus('23-D-40323', 'Wrightbus', 12.0, 2.52, 2.8,
              54, seat_belts=True)
    return bus


def bus_23487():
    """Create a Bus object for bus with registration number '23-D-23487'."""
    bus = Bus('23-D-23487', 'Wrightbus', 11.5, 2.50, 2.6,
              55, seat_belts=True)
    return bus


def bus_service_101():
    """Create a BusService object for service '101' from Drogheda to Dublin."""
    service = BusService('101', 'Drogheda-Dublin')
    service.set_bus_station_list(['Drogheda Bus Station', "St. Mary's Hospital", 'Drogheda Rail Stn'])

    service.add_bus(bus_34058())
    service.add_bus(bus_41353())
    return service


def bus_service_D1():
    """Create a BusService object for service 'D1' from Drogheda to Laytown."""
    service = BusService('D1', 'Drogheda-Laytown')
    service.set_bus_station_list(['Alverno Terrace', 'Netterville Terrace', 'Church Road', 'Sacred Heart Church',
                                  'Brookeside', 'Bettystown', 'Narrow Ways'])

    service.add_bus(bus_43060())
    service.add_bus(bus_40323())
    service.add_bus(bus_23487())
    return service


def drogheda_town_bus_services():
    """Create a BusServices object for all bus services in Drogheda Town."""
    services = BusServices('Drogheda Town Bus Services')

    services.add_bus_service(bus_service_101())
    services.add_bus_service(bus_service_D1())
    return services


def bus_traffic_41353():
    """Create a BusTraffic object for bus with registration number '20-D-41353' and add passengers."""
    service_101 = bus_service_101()
    bus = service_101.get_bus_by_registration_number('20-D-41353')
    bus_traffic = BusDriverManager('Nikita Smiichyk', bus)

    passenger1 = Passenger('Anita Smiichyk', True)
    passenger2 = Passenger('Dariia Shcherbenko', True)

    bus_traffic.add_passengers(passenger1, passenger2)
    return bus_traffic


if __name__ == '__main__':
    bus_41353().show_information()
    bus_service_101().show_information()
    bus_traffic_41353().show_information()
