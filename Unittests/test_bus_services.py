import unittest
from bus_service import BusService
from bus_services import BusServices


class TsetBusServices(unittest.TestCase):

    def setUp(self):
        self.bus_service = BusServices('Town Bus Services')

    def test_init(self):
        self.assertEqual(self.bus_service.services_name, 'Town Bus Services')
        self.assertEqual(self.bus_service.bus_service_list, [])

        # testing set_service_name() function
        self.bus_service.set_services_name('Drogheda Town Bus Services')
        self.assertEqual(self.bus_service.services_name, 'Drogheda Town Bus Services')

    def test_bus_services_list(self):
        bus_service1 = BusService('001', '0123-4567')
        bus_service2 = BusService('002', '4567-7890')

        # testing add_bus_service() function
        self.bus_service.add_bus_service(bus_service1)
        self.bus_service.add_bus_service(bus_service2)
        self.assertEqual(self.bus_service.bus_service_list, [bus_service1, bus_service2])

        # testing remove_bus_service() function
        self.bus_service.remove_bus_service(bus_service1)
        self.assertEqual(self.bus_service.bus_service_list, [bus_service2])


if __name__ == '__main__':
    unittest.main()
