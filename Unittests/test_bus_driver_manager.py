import unittest
from bus import Bus
from passenger import Passenger
from bus_driver_manager import BusDriverManager


class TestBusDriverManager(unittest.TestCase):

    def setUp(self):
        self.bus = Bus('22-D-34058', 'name', 0, 5, 4, 76)
        self.aBusDriverManager = BusDriverManager('drivers_name', self.bus)

    def test_init(self):
        # test the initialization of BusDriverManager object
        self.aBusDriverManager.set_driver('new_driver')
        self.assertEqual(self.aBusDriverManager.driver, 'new_driver')
        self.assertEqual(self.aBusDriverManager.drivers_bus, self.bus)
        self.assertEqual(self.aBusDriverManager.passenger_list, [])

        # testing get_seating_capacity() function
        self.assertEqual(self.aBusDriverManager.get_seating_capacity(), 76)

    def test_passenger_list(self):
        bus = Bus('22-D-34058', 'name', 0, 0, 0, 3)
        aBusDriverManager = BusDriverManager('drivers_name', bus)
        passenger1 = Passenger('name1', True)
        passenger2 = Passenger('name2', True)
        passenger3 = Passenger('name3', True)
        passenger4 = Passenger('name4', True)

        # Add passengers to the bus, but the capacity is only 3, so the fourth passenger should not be admitted
        aBusDriverManager.add_passengers(passenger1, passenger2, passenger3, passenger4)
        self.assertEqual(aBusDriverManager.passenger_list, [passenger1, passenger2, passenger3])

        # testing remove_passenger() function
        aBusDriverManager.remove_passenger(passenger3)
        self.assertEqual(aBusDriverManager.get_passengers(), [passenger1, passenger2])


if __name__ == '__main__':
    unittest.main()
