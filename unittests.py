import unittest
import customer
import dish
import restaurant


class TestOrder(unittest.TestCase):
    restaurant = None

    @classmethod
    def setUpClass(cls):
        # called one time, at beginning
        print('setUpClass()')
        menu
        cls.restaurant
