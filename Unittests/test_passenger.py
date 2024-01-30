import unittest
from passenger import Passenger


class TestPassenger(unittest.TestCase):

    def setUp(self):
        # Create a Passenger object
        self.passenger = Passenger('John Surname')

    def test_init(self):
        # test the initialization of Passenger object
        self.assertEqual(self.passenger.passenger_name, 'John Surname')
        self.assertFalse(self.passenger.payment_status)

    def test_set_init(self):
        self.passenger.set_passenger_name('Nikita Surname')
        self.passenger.set_payment_status(True)

        # test setting the Passenger object
        self.assertEqual(self.passenger.passenger_name, 'Nikita Surname')
        self.assertTrue(self.passenger.payment_status)


if __name__ == '__main__':
    pass
