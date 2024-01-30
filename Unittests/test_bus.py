import unittest
from bus import Bus
from bus_service import BusService
from bus_driver_manager import BusDriverManager
from passenger import Passenger


class TestBus(unittest.TestCase):

    def setUp(self):
        self.bus = Bus('20-D-41353', 'str', 1, 2, 3, 64)
        self.bus_service = BusService('name', 'town-city')

    def test_init(self):
        # test Bus class initialization
        # check if the initialized attributes match the expected values
        self.assertEqual(self.bus.registration_number, '20-D-41353')
        self.assertEqual(self.bus.year, 2020)
        self.assertEqual(self.bus.manufacturer, 'str')
        self.assertEqual(self.bus.length, 1)
        self.assertEqual(self.bus.width, 2)
        self.assertEqual(self.bus.height, 3)
        self.assertEqual(self.bus.seating_capacity, 64)

        # check the default values for additional attributes
        self.assertEqual(self.bus.floors_number, 1)
        self.assertEqual(self.bus.seat_belts, False)

    def test_calc_dimension(self):
        # test Bus dimension calculation

        # if seating_capacity >= 110: EXTRA_LARGE = 'Extra Large'
        # if seating_capacity 65 - 100: LARGE = 'Large'
        # if seating_capacity 40 - 64: AVERAGE = 'Average'
        # if seating_capacity 35 - 39: SMALL = 'Small'
        # if seating_capacity < 35: PARTICULARLY_SMALL = 'Particularly small'

        self.assertEqual(self.bus.AVERAGE, 'Average')
        self.assertEqual(self.bus.dimension, self.bus.AVERAGE)

        new_bus = Bus('00-0-00000', 'str', 1, 2, 3, 35)

        self.assertEqual(new_bus.dimension, 'Small')

    def test_init_bus_service(self):
        # check the attributes to use after adding the bus to the BusService class
        self.bus_service.add_bus(self.bus)
        self.assertEqual(self.bus.service_name, 'name')
        self.assertEqual(self.bus.bus_route, 'town-city')
        self.assertEqual(self.bus.bus_station_list, [])

        # check if the bus station appears after adding it to the BusService class
        self.bus_service.add_bus_station('bus_station_1')
        self.assertEqual(self.bus.bus_station_list, ['bus_station_1'])

    def test_init_bus_driver_manager(self):
        new_bus = Bus('00-0-00000', 'str', 1, 2, 3, 35)
        self.bus_service.add_bus(new_bus)
        self.bus_service.add_bus(self.bus)
        bus = self.bus_service.get_bus_by_registration_number('20-D-41353')

        aBusDriverManager = BusDriverManager('driver_name', bus)

        # check the attributes to use when adding a bus to a BusDriverManager class
        self.assertEqual(self.bus.passengers, [])

        # check if the passengers list appears after adding it to the BusDriverManager class
        passenger1 = Passenger('passenger_name1', True)
        passenger2 = Passenger('passenger_name2', True)
        aBusDriverManager.add_passengers(passenger1, passenger2)
        self.assertEqual(bus.passengers, [passenger1, passenger2])

        # test removing passengers
        aBusDriverManager.remove_passenger(passenger1)
        self.assertEqual(bus.passengers, [passenger2])


if __name__ == '__main__':
    unittest.main()
