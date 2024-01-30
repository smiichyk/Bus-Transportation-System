import unittest
from bus import Bus
from bus_service import BusService


class TestBusService(unittest.TestCase):
    def setUp(self):
        self.bus_service = BusService('040', '0123-4567')

    def test_init(self):
        # test the initialization of BusService object
        self.assertEqual(self.bus_service.service_name, '040')
        self.assertEqual(self.bus_service.bus_route, '0123-4567')
        self.assertEqual(self.bus_service.bus_station_list, [])
        self.assertEqual(self.bus_service.bus_list, [])

    def test_set_service_name(self):
        # test setting the service name of a BusService object
        self.bus_service.set_service_name('14352')
        self.assertEqual(self.bus_service.service_name, '14352')

    def test_set_bus_route(self):
        # test setting the bus route of a BusService object
        self.bus_service.set_bus_route('vadf-vafds')
        self.assertEqual(self.bus_service.bus_route, 'vadf-vafds')

    def test_bus_station_list(self):
        # test adding, setting, and removing bus stations in a BusService object
        # testing add_bus_station() function
        self.bus_service.add_bus_station('station1')
        self.bus_service.add_bus_station('station2')
        self.assertEqual(self.bus_service.bus_station_list, ['station1', 'station2'])

        # testing set_bus_station_list() function
        self.bus_service.set_bus_station_list(['station3', 'station1', 'station2', 'station4'])
        self.assertEqual(self.bus_service.bus_station_list, ['station3', 'station1', 'station2', 'station4'])

        # testing remove_bus_station() function
        self.bus_service.remove_bus_station('station1')
        self.assertEqual(self.bus_service.bus_station_list, ['station3', 'station2', 'station4'])

    def test_bus_list(self):
        # test adding, retrieving, and removing buses in a BusService object
        bus1 = Bus('22-D-34058', 'name1', 0, 5, 4, 5)
        bus2 = Bus('19-D-56452', 'name2', 2, 7, 6, 9)
        bus3 = Bus('23-D-43664', 'name3', 4, 2, 4, 5)

        # testing add_bus()
        self.bus_service.add_bus(bus1)
        self.bus_service.add_bus(bus2)
        self.bus_service.add_bus(bus3)
        self.assertEqual(self.bus_service.bus_list, [bus1, bus2, bus3])

        # testing get_bus_by_registration_number() function
        self.assertEqual(self.bus_service.get_bus_by_registration_number('19-D-56452'), bus2)

        # testing remove_bus()
        self.bus_service.remove_bus(bus2)
        self.assertEqual(self.bus_service.bus_list, [bus1, bus3])


if __name__ == '__main__':
    unittest.main()
